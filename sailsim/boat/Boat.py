from math import sqrt, pi

from sailsim.utils.constants import DENSITY_AIR, DENSITY_WATER
from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval
from sailsim.utils.coordconversion import cartToRadiusSq, cartToArg

from sailsim.boat.BoatDataHolder import BoatDataHolder
from sailsim.boat.coefficientsapprox import coefficientAirDrag, coefficientAirLift, coefficientWaterDrag, coefficientWaterLift


class Boat:
    """Holds all information about the boat and calculates its speed, forces and torques."""

    from .boatgetset import setBoat, getPos, getSpeed, setDirection, setMainSailAngle, setMainSailAngleDeg, setConstants

    def __init__(self, posX=0, posY=0, direction=0, speedX=0, speedY=0):
        """
        Create a boat.

        Args:
            posX:       x position of the boat (in m)
            posY:       y position of the boat (in m)
            direction:  direction the boat is pointing
            speedX:     speed in x direction (in m/s)
            speedY:     speed in y direction (in m/s)
        """
        # Dynamic properties
        self.posX = posX
        self.posY = posY

        self.speedX = speedX
        self.speedY = speedY
        self.direction = directionKeepInterval(direction)

        self.rudderAngle = 0
        self.maxRudderAngle = 80 / 180 * pi

        self.mainSailAngle = 0
        self.maxMainSailAngle = 80 / 180 * pi

        self.dataHolder = BoatDataHolder()
        self.sailor = None


        # Static properties
        self.mass = 80
        self.sailArea = 7.45
        self.hullArea = 4 # arbitrary
        self.centerboardArea = 1


        # Coefficients methods
        self.coefficientAirDrag = coefficientAirDrag
        self.coefficientAirLift = coefficientAirLift
        self.coefficientWaterDrag = coefficientWaterDrag
        self.coefficientWaterLift = coefficientWaterLift

        self.tackingAngleUpwind = 45 / 180 * pi
        self.tackingAngleDownwind = 20 / 180 * pi


    # Simulation
    def applyForce(self, forceX, forceY, interval):
        """Change speed according a force given."""
        # △v = a * t ; F = m * a
        # △v = F / m * t
        self.speedX += forceX / self.mass * interval
        self.speedY += forceY / self.mass * interval

    def moveInterval(self, interval):
        """Change position according to sailsDirection and speed."""
        # s = v * t
        self.posX += self.speedX * interval
        self.posY += self.speedY * interval

    def runSailor(self):
        """Activate the sailing algorithm to decide what the boat should do."""
        self.sailor.run(self.posX, self.posY, self.dataHolder.boatSpeed, cartToArg(self.speedX, self.speedY), self.direction, self.dataHolder.apparentWindSpeed, self.dataHolder.apparentWindAngle) # Run sailor

        # Set boat properties
        # TODO calculate mainSailAngle and import it here
        # self.mainSailAngle = self.sailor.mainSailAngle
        self.direction = self.sailor.boatDirection


    # Force calculations
    def resultingForce(self, trueWindX, trueWindY):
        """Add up all reacting forces and return them as a tuple."""
        h = self.dataHolder

        # calculate apparent wind angle
        (h.apparentWindX, h.apparentWindY) = self.apparentWind(trueWindX, trueWindY)
        h.apparentWindAngle = self.apparentWindAngle(h.apparentWindX, h.apparentWindY)

        apparentWindSpeedSq = cartToRadiusSq(h.apparentWindX, h.apparentWindY)
        h.apparentWindSpeed = sqrt(apparentWindSpeedSq)
        boatSpeedSq = self.boatSpeedSq()
        h.boatSpeed = sqrt(boatSpeedSq)

        # normalise apparent wind vector and boat speed vetor
        # if vector is (0, 0) set normalised vector to (0, 0) aswell
        (apparentWindNormX, apparentWindNormY) = (h.apparentWindX / h.apparentWindSpeed, h.apparentWindY / h.apparentWindSpeed) if not h.apparentWindSpeed == 0 else (0, 0) # normalised apparent wind vector
        (speedNormX, speedNormY) = (self.speedX / h.boatSpeed, self.speedY / h.boatSpeed) if not h.boatSpeed == 0 else (0, 0) # normalised speed vector

        h.leewayAngle = self.calcLeewayAngle()
        h.angleOfAttack = self.angleOfAttack(h.apparentWindAngle)

        # Sum up all acting forces
        (forceX, forceY) = (0, 0)
        (h.sailDragX, h.sailDragY) = self.sailDrag(apparentWindNormX, apparentWindNormY, apparentWindSpeedSq)
        forceX += h.sailDragX
        forceY += h.sailDragY
        (h.sailLiftX, h.sailLiftY) = self.sailLift(apparentWindNormX, apparentWindNormY, apparentWindSpeedSq)
        forceX += h.sailLiftX
        forceY += h.sailLiftY

        (h.waterDragX, h.waterDragY) = self.waterDrag(speedNormX, speedNormY, boatSpeedSq)
        forceX += h.waterDragX
        forceY += h.waterDragY
        (h.waterLiftX, h.waterLiftY) = self.waterLift(speedNormX, speedNormY, boatSpeedSq)
        forceX += h.waterLiftX
        forceY += h.waterLiftY

        (h.forceX, h.forceY) = (forceX, forceY)
        return (forceX, forceY)

    def sailDrag(self, apparentWindNormX, apparentWindNormY, apparentWindSpeedSq):
        """Calculate the force that is created when wind blows against the boat."""
        force = 0.5 * DENSITY_AIR * self.sailArea * apparentWindSpeedSq * self.coefficientAirDrag(self.dataHolder.angleOfAttack)
        return (force * apparentWindNormX, force * apparentWindNormY)

    def sailLift(self, apparentWindNormX, apparentWindNormY, apparentWindSpeedSq):
        """Calculate the lift force that is created when the wind changes its direction in the sail."""
        force = 0.5 * DENSITY_AIR * self.sailArea * apparentWindSpeedSq * self.coefficientAirLift(self.dataHolder.angleOfAttack)
        if self.dataHolder.angleOfAttack < 0:
            return (-force * apparentWindNormY, force * apparentWindNormX)  # rotate by 90° counterclockwise
        return (force * apparentWindNormY, -force * apparentWindNormX)      # rotate by 90° clockwise

    def waterDrag(self, speedNormX, speedNormY, boatSpeedSq):
        """Calculate the drag force of the water that is decelerating the boat."""
        force = -0.5 * DENSITY_WATER * (self.hullArea + self.centerboardArea) * boatSpeedSq * self.coefficientWaterDrag(self.dataHolder.leewayAngle)
        return (force * speedNormX, force * speedNormY) # TODO waterDrag

    def waterLift(self, speedNormX, speedNormY, boatSpeedSq):
        """Calculate force that is caused by lift forces in the water."""
        force = -0.5 * DENSITY_WATER * self.centerboardArea * boatSpeedSq * self.coefficientWaterLift(self.dataHolder.leewayAngle)
        if self.dataHolder.leewayAngle < 0:
            return (-force * speedNormY, force * speedNormX)    # rotate by 90° counterclockwise
        return (force * speedNormY, -force * speedNormX)        # rotate by 90° clockwise


    # Speed calculations
    def boatSpeedSq(self):
        """Return speed of the boat but squared."""
        return pow(self.speedX, 2) + pow(self.speedY, 2)

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
        return "Boat @(%s|%s), v=%sm/s twds %s°" % (round(self.posX, 3), round(self.posY, 3), round(sqrt(self.boatSpeedSq()), 2), heading)
