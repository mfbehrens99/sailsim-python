from math import sqrt, pi, sin, cos

from sailsim.boat.FrameList import FrameList
from sailsim.sailor.Sailor import Sailor
from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval
from sailsim.utils.coordconversion import cartToRadiusSq, cartToArg
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

    temp_forceX: float
    temp_forceY: float
    temp_sailDragX: float
    temp_sailDragY: float
    temp_sailLiftX: float
    temp_sailLiftY: float
    temp_centerboardDragX: float
    temp_centerboardDragY: float
    temp_centerboardLiftX: float
    temp_centerboardLiftY: float
    temp_rudderDragX: float
    temp_rudderDragY: float
    temp_rudderLiftX: float
    temp_rudderLiftY: float

    temp_torque: float
    temp_waterDragTorque: float
    temp_rudderTorque: float
    temp_centerboardTorque: float

    sailor: Sailor

    def __init__(self, posX: float = 0, posY: float = 0, direction: float = 0, speedX: float = 0, speedY: float = 0, angSpeed: float = 0) -> None:
        """
        Create a boat.

        Args:
            posX:       x position of the boat (in m)
            posY:       y position of the boat (in m)
            direction:  direction the boat is pointing (in rad)
            speedX:     speed in x direction (in m/s)
            speedY:     speed in y direction (in m/s)
            angSpeed:   angular speed in z direction (in rad/s)
        """
        # Static properties
        self.length: float = 4.2               # m
        self.width: float = 1.63               # m
        self.mass: float = 80                  # kg
        self.momentumInertia: float = 1/12 * self.mass * (pow(self.length, 2) + pow(self.width, 2))  # kg/m^2
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
        self.posX: float = posX
        self.posY: float = posY
        self.speedX: float = speedX
        self.speedY: float = speedY

        self.direction: float = directionKeepInterval(direction)
        self.angSpeed: float = angSpeed        # rad/s
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
    def applyCauses(self, forceX: float, forceY: float, torque: float, interval: float) -> None:
        """Change speed according a force & torque given."""
        # Translation: △v = a * t; F = m * a -> △v = F / m * t
        # Rotation:    △ω = α * t; M = I * α -> △ω = M / I * t
        self.speedX += forceX / self.mass * interval
        self.speedY += forceY / self.mass * interval
        self.angSpeed += torque / self.momentumInertia * interval

    def moveInterval(self, interval: float) -> None:
        """Change position according to sailsDirection and speed."""
        # △s = v * t; △α = ω * t
        self.posX += self.speedX * interval
        self.posY += self.speedY * interval
        self.direction = directionKeepInterval(self.direction + self.angSpeed * interval)

    def runSailor(self) -> None:
        """Activate the sailing algorithm to decide what the boat should do."""
        if self.sailor is not None:
            # Run sailor if sailor exists
            self.sailor.run(
                self.posX,
                self.posY,
                self.temp_boatSpeed,
                cartToArg(self.speedX, self.speedY),
                self.direction,
                self.temp_apparentWindSpeed,
                self.temp_apparentWindAngle
            )

            # Retrieve boat properties from Sailor
            self.mainSailAngle = self.sailor.mainSailAngle
            # self.direction = self.sailor.boatDirection
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

    def resultingCauses(self) -> tuple[float, float, float]:
        """Add up all acting forces and return them as a tuple."""
        # calculate flowSpeed
        (flowSpeedRudderX, flowSpeedRudderY) = self.leverSpeedVector(self.rudderLever)
        flowSpeedRudderSq = cartToRadiusSq(flowSpeedRudderX, flowSpeedRudderY)
        flowSpeedRudder = sqrt(flowSpeedRudderSq)

        (flowSpeedCenterboardX, flowSpeedCenterboardY) = self.leverSpeedVector(self.centerboardLever)
        flowSpeedCenterboardSq = cartToRadiusSq(flowSpeedCenterboardX, flowSpeedCenterboardY)
        flowSpeedCenterboard = sqrt(flowSpeedCenterboardSq)

        # normalise apparent wind vector and boat speed vector
        (dirNormX, dirNormY) = (sin(self.direction), cos(self.direction))
        # if vector is (0, 0) set normalised vector to (0, 0) as well
        (apparentWindNormX, apparentWindNormY) = (self.temp_apparentWindX / self.temp_apparentWindSpeed, self.temp_apparentWindY / self.temp_apparentWindSpeed) if not self.temp_apparentWindSpeed == 0 else (0, 0) # normalised apparent wind vector
        # (speedNormX, speedNormY) = (self.speedX / self.temp_boatSpeed, self.speedY / self.temp_boatSpeed) if not self.temp_boatSpeed == 0 else (0, 0) # normalized speed vector
        (flowSpeedRudderNormX, flowSpeedRudderNormY) = (flowSpeedRudderX / flowSpeedRudder, flowSpeedRudderY / flowSpeedRudder) if not flowSpeedRudder == 0 else (0, 0) # normalised speed vector
        (flowSpeedCenterboardNormX, flowSpeedCenterboardNormY) = (flowSpeedCenterboardX / flowSpeedCenterboard, flowSpeedCenterboardY / flowSpeedCenterboard) if not flowSpeedCenterboard == 0 else (0, 0) # normalised speed vector

        # Sail forces
        (self.temp_sailDragX, self.temp_sailDragY) = self.sailDrag(self.temp_apparentWindSpeed, apparentWindNormX, apparentWindNormY)
        (self.temp_sailLiftX, self.temp_sailLiftY) = self.sailLift(self.temp_apparentWindSpeed, apparentWindNormX, apparentWindNormY)

        # Centerboard forces
        (self.temp_centerboardDragX, self.temp_centerboardDragY) = self.centerboardDrag(flowSpeedCenterboardSq, flowSpeedCenterboardNormX, flowSpeedCenterboardNormY)
        (self.temp_centerboardLiftX, self.temp_centerboardLiftY) = self.centerboardLift(flowSpeedCenterboardSq, flowSpeedCenterboardNormX, flowSpeedCenterboardNormY)

        # Rudder forces
        (self.temp_rudderDragX, self.temp_rudderDragY) = self.rudderDrag(flowSpeedRudderSq, flowSpeedRudderNormX, flowSpeedRudderNormY)
        (self.temp_rudderLiftX, self.temp_rudderLiftY) = self.rudderLift(flowSpeedRudderSq, flowSpeedRudderNormX, flowSpeedRudderNormY)

        # TODO Hull forces

        # Torques
        self.temp_waterDragTorque = self.waterDragTorque()
        self.temp_centerboardTorque = self.centerboardTorque(self.temp_centerboardDragX + self.temp_centerboardLiftX, self.temp_centerboardDragY + self.temp_centerboardLiftY, dirNormX, dirNormY)
        self.temp_rudderTorque = self.rudderTorque(self.temp_rudderDragX + self.temp_rudderLiftX, self.temp_rudderDragY + self.temp_rudderLiftY, dirNormX, dirNormY)

        self.temp_forceX = self.temp_sailDragX + self.temp_sailLiftX + self.temp_centerboardDragX + self.temp_centerboardLiftX + self.temp_rudderDragX + self.temp_rudderLiftX
        self.temp_forceY = self.temp_sailDragY + self.temp_sailLiftY + self.temp_centerboardDragY + self.temp_centerboardLiftY + self.temp_rudderDragY + self.temp_rudderLiftY
        self.temp_torque = self.temp_waterDragTorque + self.temp_centerboardTorque + self.temp_rudderTorque

        return (self.temp_forceX, self.temp_forceY, self.temp_torque)

    # Import force and torque functions
    from sailsim.boat.boat_forces import leverSpeedVector, sailDrag, sailLift, centerboardDrag, centerboardLift, rudderDrag, rudderLift, scalarToDragForce, scalarToLiftForce
    from sailsim.boat.boat_torques import waterDragTorque, centerboardTorque, rudderTorque

    def boatSpeed(self) -> float:
        """Return speed of the boat."""
        return sqrt(pow(self.speedX, 2) + pow(self.speedY, 2))

    # Angle calculations
    def calcLeewayAngle(self) -> float:
        """Calculate and return the leeway angle."""
        return angleKeepInterval(cartToArg(self.speedX, self.speedY) - self.direction)

    def apparentWind(self, trueWindX: float, trueWindY: float) -> tuple[float, float]:
        """Return apparent wind by adding true wind and speed."""
        return (trueWindX - self.speedX, trueWindY - self.speedY)

    def apparentWindAngle(self, apparentWindX: float, apparentWindY: float) -> float:
        """Calculate the apparent wind angle based on the carthesian true wind."""
        return angleKeepInterval(cartToArg(apparentWindX, apparentWindY) - self.direction)

    def angleOfAttack(self, apparentWindAngle: float) -> float:
        """Calculate angle between main sail and apparent wind vector."""
        return angleKeepInterval(apparentWindAngle - self.mainSailAngle + pi)

    def __repr__(self) -> str:
        heading: float = round(cartToArg(self.speedX, self.speedY) * 180 / pi, 2)
        return f"Boat @({round(self.posX, 3)}|{round(self.posY, 3)}|{heading}°), v={round(self.boatSpeed(), 2)}m/s"
