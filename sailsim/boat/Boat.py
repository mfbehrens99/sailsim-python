"""This file contains the boat class."""

from numpy import sqrt, pi, sin, cos, array, ndarray, zeros
from numpy.linalg import norm

from sailsim.boat.FrameList import FrameList
from sailsim.sailor.Sailor import Sailor
from sailsim.utils.anglecalculations import angleKeepInterval
from sailsim.utils.coordconversion import cartToRadiusSq, cartToArg
from sailsim.utils import Wrench
from sailsim.boat.coefficientsapprox import coefficientAirDrag, coefficientAirLift, coefficientWaterDrag, coefficientWaterLift


class Boat:
    """Holds all information about the boat and calculates its speed, forces and torques."""

    from sailsim.boat.boat_getset import setBoat, getPos, getSpeed, setDirection, setDirectionDeg, setMainSailAngle, setMainSailAngleDeg, setRudderAngle, setRudderAngleDeg, setConstants

    # Temporary Values
    temp_boatSpeed: float
    temp_apparentWindSpeed: float

    temp_apparentWindX: float
    temp_apparentWindY: float
    temp_apparentWindAngle: float
    temp_leewayAngle: float
    temp_angleOfAttack: float

    temp_wrench: Wrench
    temp_sailDrag: Wrench
    temp_sailLift: Wrench
    temp_centerboardDrag: Wrench
    temp_centerboardLift: Wrench
    temp_rudderDrag: Wrench
    temp_rudderLift: Wrench
    temp_hullDrag: Wrench

    sailor: Sailor

    def __init__(self, pose: ndarray = zeros(3), speed: ndarray = zeros(3)) -> None:
        """
        Create a boat.

        Args:
            pose:       position and orientation of the boat (in m or rad) (x, y, direction)
            speed:      speed (in m/s or rad/s) (x, y, angular)
        """
        # Static properties
        self.length: float = 4.2               # m
        self.width: float = 1.63               # m
        self.mass: float = 80                  # kg
        self.momentumInertia: float = 1 / 12 * self.mass * (pow(self.length, 2) + pow(self.width, 2))  # kg/m^2
        self.sailArea: float = 7.45            # m^2
        self.hullArea: float = 4               # m^2
        self.centerboardArea: float = 1        # m^2 # self.centerboardDepth * self.centerboardLength
        self.centerboardDepth: float = 0       # m
        self.centerboardLength: float = 0      # m
        self.centerboardLever: float = -0.3    # m
        self.rudderArea: float = .175          # m^2 # self.rudderDepth * self.rudderLength
        self.rudderDepth: float = 0            # m
        self.rudderLength: float = 0           # m
        self.rudderLever: float = 2.1          # m

        # Dynamic properties
        self.pose: ndarray = pose
        self.speed: ndarray = speed

        self.pivot: float = 0.5 * self.length  # m

        self.mainSailAngle: float = 0
        self.maxMainSailAngle: float = 80 / 180 * pi
        self.rudderAngle: float = 0
        self.maxRudderAngle: float = 80 / 180 * pi

        # Coefficients methods
        self.coefficientAirDrag = coefficientAirDrag
        self.coefficientAirLift = coefficientAirLift
        self.coefficientWaterDrag = coefficientWaterDrag
        self.coefficientWaterLift = coefficientWaterLift

        self.tackingAngleUpwind: float = 45 / 180 * pi
        self.tackingAngleDownwind: float = 20 / 180 * pi

        self.frameList: FrameList = FrameList()

    # Simulation methods
    def applyCauses(self, wrench: Wrench, interval: float) -> None:
        """Change speed according a force & torque given."""
        # Translation: △v = a * t; F = m * a -> △v = F / m * t
        # Rotation:    △ω = α * t; M = I * α -> △ω = M / I * t
        self.speed = self.speed + wrench / array([self.mass, self.mass, self.momentumInertia], dtype=float) * interval

    def moveInterval(self, interval: float) -> None:
        """Change position according to sailsDirection and speed."""
        # △s = v * t; △α = ω * t
        self.pose = self.pose + self.speed * interval

    def runSailor(self) -> None:
        """Activate the sailing algorithm to decide what the boat should do."""
        if self.sailor is not None:
            # Run sailor if sailor exists
            self.sailor.run(
                self.pose[0],
                self.pose[1],
                self.temp_boatSpeed,
                cartToArg(self.speed[0], self.speed[1]),
                self.pose[2],
                self.temp_apparentWindSpeed,
                self.temp_apparentWindAngle
            )

            # Retrieve boat properties from Sailor
            self.mainSailAngle = self.sailor.mainSailAngle
            self.rudderAngle = self.sailor.rudderAngle

    def updateTemporaryData(self, trueWindX: float, trueWindY: float) -> None:
        """Update values of temporary variables."""
        self.temp_boatSpeed = self.boatSpeed()

        # calculate apparent wind angle
        (self.temp_apparentWindX, self.temp_apparentWindY) = self.apparentWind(trueWindX, trueWindY)
        self.temp_apparentWindAngle = self.apparentWindAngle(self.temp_apparentWindX, self.temp_apparentWindY)
        self.temp_apparentWindSpeed = sqrt(cartToRadiusSq(self.temp_apparentWindX, self.temp_apparentWindY))

        self.temp_leewayAngle = self.calcLeewayAngle()
        self.temp_angleOfAttack = self.angleOfAttack(self.temp_apparentWindAngle)

    def resultingCauses(self) -> Wrench:
        """Add up all acting forces and return them as a tuple."""
        # calculate flowSpeed
        (flowSpeedRudderX, flowSpeedRudderY) = self.leverSpeedVector(self.rudderLever)
        flowSpeedRudderSq = cartToRadiusSq(flowSpeedRudderX, flowSpeedRudderY)
        flowSpeedRudder = sqrt(flowSpeedRudderSq)

        (flowSpeedCenterboardX, flowSpeedCenterboardY) = self.leverSpeedVector(self.centerboardLever)
        flowSpeedCenterboardSq = cartToRadiusSq(flowSpeedCenterboardX, flowSpeedCenterboardY)
        flowSpeedCenterboard = sqrt(flowSpeedCenterboardSq)

        # normalize apparent wind vector and boat speed vector
        dirNorm = array([sin(self.pose[2]), cos(self.pose[2])])
        # if vector is (0, 0) set normalized vector to (0, 0) as well
        apparentWindNorm: ndarray = array([self.temp_apparentWindX, self.temp_apparentWindY]) / self.temp_apparentWindSpeed if not self.temp_apparentWindSpeed == 0 else zeros(2)  # normalized apparent wind vector
        flowSpeedRudderNorm: ndarray = array([flowSpeedRudderX, flowSpeedRudderY]) / flowSpeedRudder if not flowSpeedRudder == 0 else zeros(2)  # normalized speed vector
        flowSpeedCenterboardNorm: ndarray = array([flowSpeedCenterboardX, flowSpeedCenterboardY]) / flowSpeedCenterboard if not flowSpeedCenterboard == 0 else zeros(2)  # normalized speed vector

        # Sail forces
        self.temp_sailDrag = self.sailDrag(self.temp_apparentWindSpeed, apparentWindNorm)
        self.temp_sailLift = self.sailLift(self.temp_apparentWindSpeed, apparentWindNorm)

        # Centerboard forces
        self.temp_centerboardDrag = self.centerboardDrag(flowSpeedCenterboardSq, flowSpeedCenterboardNorm, dirNorm)
        self.temp_centerboardLift = self.centerboardLift(flowSpeedCenterboardSq, flowSpeedCenterboardNorm, dirNorm)

        # Rudder forces
        self.temp_rudderDrag = self.rudderDrag(flowSpeedRudderSq, flowSpeedRudderNorm, dirNorm)
        self.temp_rudderLift = self.rudderLift(flowSpeedRudderSq, flowSpeedRudderNorm, dirNorm)

        # TODO Hull forces
        self.temp_hullDrag = self.waterDrag()

        self.temp_wrench = (self.temp_sailDrag + self.temp_sailLift + self.temp_centerboardDrag + self.temp_centerboardLift + self.temp_rudderDrag + self.temp_rudderLift + self.temp_hullDrag).view(Wrench)
        return self.temp_wrench

    # Import force and torque functions
    from sailsim.boat.boat_forces import leverSpeedVector, sailDrag, sailLift, centerboardDrag, centerboardLift, rudderDrag, rudderLift, waterDrag, scalarToLiftForce

    def boatSpeed(self) -> float:
        """Return speed of the boat."""
        return float(norm(self.speed[:2]))

    # Angle calculations
    def calcLeewayAngle(self) -> float:
        """Calculate and return the leeway angle."""
        return angleKeepInterval(cartToArg(self.speed[0], self.speed[1]) - self.pose[2])

    def apparentWind(self, trueWindX: float, trueWindY: float) -> tuple[float, float]:
        """Return apparent wind by adding true wind and speed."""
        return (trueWindX - self.speed[0], trueWindY - self.speed[1])

    def apparentWindAngle(self, apparentWindX: float, apparentWindY: float) -> float:
        """Calculate the apparent wind angle based on the Cartesian true wind."""
        return angleKeepInterval(cartToArg(apparentWindX, apparentWindY) - self.pose[2])

    def angleOfAttack(self, apparentWindAngle: float) -> float:
        """Calculate angle between main sail and apparent wind vector."""
        return angleKeepInterval(apparentWindAngle - self.mainSailAngle + pi)

    def __repr__(self) -> str:
        """Generate a descriptive text for the boat."""
        heading: float = round(cartToArg(self.speed[0], self.speed[1]) * 180 / pi, 2)
        return f"Boat @({round(self.pose[0], 3)}|{round(self.pose[1], 3)}|{heading}°), v={round(self.boatSpeed(), 2)}m/s"
