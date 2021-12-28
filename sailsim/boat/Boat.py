from math import sqrt, pi, sin, cos
from sailsim.boat.FrameList import FrameList

from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval
from sailsim.utils.coordconversion import cartToRadiusSq, cartToArg

from sailsim.boat.BoatDataHolder import BoatDataHolder
from sailsim.boat.coefficientsapprox import coefficientAirDrag, coefficientAirLift, coefficientWaterDrag, coefficientWaterLift


class Boat:
    """Holds all information about the boat and calculates its speed, forces and torques."""

    from .boatgetset import setBoat, getPos, getSpeed, setDirection, setDirectionDeg, setMainSailAngle, setMainSailAngleDeg, setRudderAngle, setRudderAngleDeg, setConstants

    def __init__(self, posX=0, posY=0, direction=0, speedX=0, speedY=0, angSpeed=0):
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
        self.length = 4.2               # m
        self.width = 1.63               # m
        self.mass = 80                  # kg
        self.momentumInertia = 1/12 * self.mass * (pow(self.length, 2) + pow(self.width, 2))  # kg/m^2
        self.sailArea = 7.45            # m^2
        self.hullArea = 4               # m^2
        self.centerboardArea = 1        # m^2 # self.centerboardDepth * self.centerboardLength
        self.centerboardDepth = 0       # m
        self.centerboardLength = 0      # m
        self.centerboardLever = -0.3    # m
        self.rudderArea = .175          # m^2 # self.rudderDepth * self.rudderLength
        self.rudderDepth = 0            # m
        self.rudderLength = 0           # m
        self.rudderLever = 2.1          # m

        # Dynamic properties
        self.posX = posX
        self.posY = posY
        self.speedX = speedX
        self.speedY = speedY

        self.direction = directionKeepInterval(direction)
        self.angSpeed = angSpeed        # rad/s
        self.pivot = 0.5 * self.length  # m

        self.mainSailAngle = 0
        self.maxMainSailAngle = 80 / 180 * pi

        self.rudderAngle = 0
        self.maxRudderAngle = 80 / 180 * pi

        self.dataHolder = BoatDataHolder()
        self.sailor = None

        # Coefficients methods
        self.coefficientAirDrag = coefficientAirDrag
        self.coefficientAirLift = coefficientAirLift
        self.coefficientWaterDrag = coefficientWaterDrag
        self.coefficientWaterLift = coefficientWaterLift

        self.tackingAngleUpwind = 45 / 180 * pi
        self.tackingAngleDownwind = 20 / 180 * pi

        self.frameList = FrameList()


    # Simulation methods
    def applyCauses(self, forceX, forceY, torque, interval):
        """Change speed according a force & torque given."""
        # Translation: △v = a * t; F = m * a -> △v = F / m * t
        # Rotation:    △ω = α * t; M = I * α -> △ω = M / I * t
        self.speedX += forceX / self.mass * interval
        self.speedY += forceY / self.mass * interval
        self.angSpeed += torque / self.momentumInertia * interval

    def moveInterval(self, interval):
        """Change position according to sailsDirection and speed."""
        # △s = v * t; △α = ω * t
        self.posX += self.speedX * interval
        self.posY += self.speedY * interval
        self.direction = directionKeepInterval(self.direction + self.angSpeed * interval)

    def runSailor(self):
        """Activate the sailing algorithm to decide what the boat should do."""
        if self.sailor is not None:
            # Run sailor if sailor exists
            self.sailor.run(
                self.posX,
                self.posY,
                self.dataHolder.boatSpeed,
                cartToArg(self.speedX, self.speedY),
                self.direction,
                self.dataHolder.apparentWindSpeed,
                self.dataHolder.apparentWindAngle
            )

            # Retrieve boat properties from Sailor
            self.mainSailAngle = self.sailor.mainSailAngle
            # self.direction = self.sailor.boatDirection
            self.rudderAngle = self.sailor.rudderAngle

    def resultingCauses(self, trueWindX, trueWindY):
        """Add up all acting forces and return them as a tuple."""
        h = self.dataHolder

        h.boatSpeed = self.boatSpeed()

        # calculate apparent wind angle
        (h.apparentWindX, h.apparentWindY) = self.apparentWind(trueWindX, trueWindY)
        h.apparentWindAngle = self.apparentWindAngle(h.apparentWindX, h.apparentWindY)
        apparentWindSpeedSq = cartToRadiusSq(h.apparentWindX, h.apparentWindY)
        h.apparentWindSpeed = sqrt(apparentWindSpeedSq)

        # calculate flowSpeed
        (flowSpeedRudderX, flowSpeedRudderY) = self.leverSpeedVector(self.rudderLever)
        flowSpeedRudderSq = cartToRadiusSq(flowSpeedRudderX, flowSpeedRudderY)
        flowSpeedRudder = sqrt(flowSpeedRudderSq)

        (flowSpeedCenterboardX, flowSpeedCenterboardY) = self.leverSpeedVector(self.centerboardLever)
        flowSpeedCenterboardSq = cartToRadiusSq(flowSpeedCenterboardX, flowSpeedCenterboardY)
        flowSpeedCenterboard = sqrt(flowSpeedCenterboardSq)

        # normalise apparent wind vector and boat speed vetor
        # if vector is (0, 0) set normalised vector to (0, 0) aswell
        (apparentWindNormX, apparentWindNormY) = (h.apparentWindX / h.apparentWindSpeed, h.apparentWindY / h.apparentWindSpeed) if not h.apparentWindSpeed == 0 else (0, 0) # normalised apparent wind vector
        # (speedNormX, speedNormY) = (self.speedX / h.boatSpeed, self.speedY / h.boatSpeed) if not h.boatSpeed == 0 else (0, 0) # normalised speed vector
        (flowSpeedRudderNormX, flowSpeedRudderNormY) = (flowSpeedRudderX / flowSpeedRudder, flowSpeedRudderY / flowSpeedRudder) if not flowSpeedRudder == 0 else (0, 0) # normalised speed vector
        (flowSpeedCenterboardNormX, flowSpeedCenterboardNormY) = (flowSpeedCenterboardX / flowSpeedCenterboard, flowSpeedCenterboardY / flowSpeedCenterboard) if not flowSpeedCenterboard == 0 else (0, 0) # normalised speed vector
        (dirNormX, dirNormY) = (sin(self.direction), cos(self.direction))

        h.leewayAngle = self.calcLeewayAngle()
        h.angleOfAttack = self.angleOfAttack(h.apparentWindAngle)


        # Sail forces
        (h.sailDragX, h.sailDragY) = self.sailDrag(apparentWindSpeedSq, apparentWindNormX, apparentWindNormY)
        (h.sailLiftX, h.sailLiftY) = self.sailLift(apparentWindSpeedSq, apparentWindNormX, apparentWindNormY)

        # Centerboard forces
        (h.centerboardDragX, h.centerboardDragY) = self.centerboardDrag(flowSpeedCenterboardSq, flowSpeedCenterboardNormX, flowSpeedCenterboardNormY)
        (h.centerboardLiftX, h.centerboardLiftY) = self.centerboardLift(flowSpeedCenterboardSq, flowSpeedCenterboardNormX, flowSpeedCenterboardNormY)

        # Rudder forces
        (h.rudderDragX, h.rudderDragY) = self.rudderDrag(flowSpeedRudderSq, flowSpeedRudderNormX, flowSpeedRudderNormY)
        (h.rudderLiftX, h.rudderLiftY) = self.rudderLift(flowSpeedRudderSq, flowSpeedRudderNormX, flowSpeedRudderNormY)

        # TODO Hull forces


        # Torques
        h.waterDragTorque = self.waterDragTorque()
        h.centerboardTorque = self.centerboardTorque(h.centerboardDragX + h.centerboardLiftX, h.centerboardDragY + h.centerboardLiftY, dirNormX, dirNormY)
        h.rudderTorque = self.rudderTorque(h.rudderDragX + h.rudderLiftX, h.rudderDragY + h.rudderLiftY, dirNormX, dirNormY)

        forceX = h.sailDragX + h.sailLiftX + h.centerboardDragX + h.centerboardLiftX + h.rudderDragX + h.rudderLiftX
        forceY = h.sailDragY + h.sailLiftY + h.centerboardDragY + h.centerboardLiftY + h.rudderDragY + h.rudderLiftY
        torque = h.waterDragTorque + h.centerboardTorque + h.rudderTorque

        (h.forceX, h.forceY, h.torque) = (forceX, forceY, torque)
        return (forceX, forceY, torque)

    # Import force and torque functions
    from .boat_forces import leverSpeedVector, sailDrag, sailLift, centerboardDrag, centerboardLift, rudderDrag, rudderLift, scalarToDragForce, scalarToLiftForce
    from .boat_torques import waterDragTorque, centerboardTorque, rudderTorque


    def boatSpeed(self):
        """Return speed of the boat."""
        return sqrt(pow(self.speedX, 2) + pow(self.speedY, 2))


    # Angle calculations
    def calcLeewayAngle(self):
        """Calculate and return the leeway angle."""
        return angleKeepInterval(cartToArg(self.speedX, self.speedY) - self.direction)

    def apparentWind(self, trueWindX, trueWindY):
        """Return apparent wind by adding true wind and speed."""
        return (trueWindX - self.speedX, trueWindY - self.speedY)

    def apparentWindAngle(self, apparentWindX, apparentWindY):
        """Calculate the apparent wind angle based on the carthesian true wind."""
        return angleKeepInterval(cartToArg(apparentWindX, apparentWindY) - self.direction)

    def angleOfAttack(self, apparentWindAngle):
        """Calculate angle between main sail and apparent wind vector."""
        return angleKeepInterval(apparentWindAngle - self.mainSailAngle + pi)


    def __repr__(self):
        heading = round(cartToArg(self.speedX, self.speedY) * 180 / pi, 2)
        return "Boat @(%s|%s), v=%sm/s twds %s°" % (round(self.posX, 3), round(self.posY, 3), round(self.boatSpeed(), 2), heading)
