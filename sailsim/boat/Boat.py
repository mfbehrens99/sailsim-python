from math import sin, sqrt, pi

from sailsim.utils.constants import DENSITY_AIR, DENSITY_WATER
from sailsim.utils.anglecalculations import angleKeepInterval
from sailsim.utils.coordconversion import cartToArg


class Boat:
    """Holds all information about the boat and calculates its speed, forces and torques."""

    def __init__(self, posX, posY, mass, area, sailor):
        # Static properties
        self.mass = mass
        self.sailArea = area
        self.hullArea = 4 # arbitrary
        self.centerboardArea = 1

        self.FORCE_CONST_AIR = 0.5 * DENSITY_AIR * self.sailArea # kg / m
        # self.FORCE_CONST_AIR_LIFT = 0.5 * DENSITY_AIR * self.sailArea
        self.FORCE_CONST_WATER = 0.5 * DENSITY_WATER * (self.hullArea + self.centerboardArea) # kg / m
        self.FORCE_CONST_WATER_LIFT = 0.5 * DENSITY_WATER * self.centerboardArea

        # Dynamic properties
        self.posX = posX
        self.posY = posY

        self.speedX = 0
        self.speedY = 0
        self.direction = 0

        self.sailor = sailor # Sail algorithm
        self.mainSailAngle = 45 * pi / 180


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
        # TODO interact with sailor library

    # Force calculations
    def resultingForce(self, trueWindX, trueWindY):
        """Add up all reacting forces and return them as a tuple."""
        # calculate apparent wind angle
        (apparentWindX, apparentWindY) = self.apparentWind(trueWindX, trueWindY)
        apparentWindAngle = self.apparentWindAngle(apparentWindX, apparentWindY)

        apparentWindSpeedSq = self.apparentWindSpeedSq(apparentWindX, apparentWindY)
        apparentWindSpeed = sqrt(apparentWindSpeedSq)
        boatSpeedSq = self.boatSpeedSq()
        boatSpeed = sqrt(boatSpeedSq)

        # normalise apparent wind vector and boat speed vetor
        # if vector is (0, 0) set normalised vector to (0, 0) aswell
        (apparentWindNormX, apparentWindNormY) = (apparentWindX / apparentWindSpeed, apparentWindY / apparentWindSpeed) if not apparentWindSpeed == 0 else (0, 0) # normalised apparent wind vector
        (speedNormX, speedNormY) = (self.speedX / boatSpeed, self.speedY / boatSpeed) if not boatSpeed == 0 else (0, 0) # normalised speed vector

        leewayAngle = self.calcLeewayAngle()
        angleOfAttack = self.angleOfAttack(apparentWindAngle)

        # print("apWind:", apparentWindX, apparentWindY)
        # print("apWindAng:", apparentWindAngle * 180 / pi)
        # print("angOfAtk:", angleOfAttack * 180 / pi)

        # Sum up all acting forces
        # FIXME check if this can be implemented nicer
        sumX, sumY = 0, 0
        (sailDragX, sailDragY) = self.sailDrag(apparentWindNormX, apparentWindNormY, apparentWindSpeedSq, angleOfAttack)
        sumX += sailDragX
        sumY += sailDragY
        (sailLiftX, sailLiftY) = self.sailLift(apparentWindNormX, apparentWindNormY, apparentWindSpeedSq, apparentWindAngle, angleOfAttack)
        sumX += sailLiftX
        sumY += sailLiftY

        (waterDragX, waterDragY) = self.waterDrag(speedNormX, speedNormY, boatSpeedSq, leewayAngle)
        sumX += waterDragX
        sumY += waterDragY
        (waterLiftX, waterLiftY) = self.waterLift(speedNormX, speedNormY, boatSpeedSq, leewayAngle, apparentWindAngle)
        sumX += waterLiftX
        sumY += waterLiftY

        # print(self.speedX, self.speedY)
        # print(sailDragX, sailDragY)
        # print(sailLiftX, sailLiftY)
        # print(waterDragX, waterDragY)
        # print(waterLiftX, waterLiftY)
        # print(sumX, sumY)
        # print("----------")

        return (sumX, sumY)

    def sailDrag(self, apparentWindNormX, apparentWindNormY, apparentWindSpeedSq, angleOfAttack):
        """Calculate the force that is created when wind blows against the boat."""
        force = self.FORCE_CONST_AIR * apparentWindSpeedSq * self.coefficientAirDrag(angleOfAttack)
        return (force * apparentWindNormX, force * apparentWindNormY)

    def sailLift(self, apparentWindNormX, apparentWindNormY, apparentWindSpeedSq, apparentWindAngle, angleOfAttack):
        """Calculate the lift force that is created when the wind changes its direction in the sail."""
        force = self.FORCE_CONST_AIR * apparentWindSpeedSq * self.coefficientAirLift(angleOfAttack)
        if angleOfAttack < 0:
            return (-force * apparentWindNormY, force * apparentWindNormX)  # rotate by 90° counterclockwise
        return (force * apparentWindNormY, -force * apparentWindNormX)      # rotate by 90° clockwise

    def waterDrag(self, speedNormX, speedNormY, boatSpeedSq, leewayAngle):
        """Calculate the drag force of the water that is decelerating the boat."""
        force = -self.FORCE_CONST_WATER * boatSpeedSq * self.coefficientWaterDrag(leewayAngle)
        return (force * speedNormX, force * speedNormY) # TODO waterDrag

    def waterLift(self, speedNormX, speedNormY, boatSpeedSq, leewayAngle, apparentWindAngle):
        """Calculate force that is caused by lift forces in the water."""
        force = -self.FORCE_CONST_WATER_LIFT * boatSpeedSq * self.coefficientWaterLift(leewayAngle)
        if leewayAngle < 0: # NOTE potential error
            return (-force * speedNormY, force * speedNormX)    # rotate by 90° counterclockwise
        return (force * speedNormY, -force * speedNormX)        # rotate by 90° clockwise


    # Coefficient calculations
    def coefficientAirDrag(self, angleOfAttack):
        """Calculate the wind resitance coefficient based on the angle of attack."""
        # NOTE function has been approximated!
        # TODO calculate coefficient using Xfoil
        return 0.41 * pow(angleOfAttack, 2) + 0.13 * abs(angleOfAttack) + 0.3

    def coefficientAirLift(self, angleOfAttack):
        """Calculate the wind lift coefficient based on the angle of attack."""
        # NOTE function has been approximated!
        # TODO calculate coefficient using Xfoil
        if abs(angleOfAttack) > 1.07:
            return 1.67
        return 11 * pow(angleOfAttack, 4) - 22.46 * pow(abs(angleOfAttack), 3) + 7.39 * pow(angleOfAttack, 2) + 5.88 * abs(angleOfAttack)

    def coefficientWaterDrag(self, angleOfAttack):
        """Calculate the water drag coefficient based on the angle of attack."""
        # NOTE function has been approximated!
        # TODO calculate coefficient using Xfoil
        return self.coefficientAirDrag(angleOfAttack)

    def coefficientWaterLift(self, angleOfAttack):
        """Calculate the water lift coefficient based on the angle of attack."""
        # NOTE function has been approximated!
        # TODO calculate coefficient using Xfoil
        return self.coefficientAirLift(angleOfAttack)


    # Speed calculations
    def boatSpeedSq(self):
        """Return speed of the boat but squared."""
        return pow(self.speedX, 2) + pow(self.speedY, 2)

    def apparentWindSpeedSq(self, apparentWindX, apparentWindY):
        """Calculate speed of apparent wind but squared."""
        return pow(apparentWindX, 2) + pow(apparentWindY, 2)


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
