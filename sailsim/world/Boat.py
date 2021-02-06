from math import sin, sqrt, pi

from sailsim.utils.constants import DENSITY_AIR, DENSITY_WATER
from sailsim.utils.coordconversion import cartToArg


class Boat:
    """Holds all information about the boat and calculates its speed, forces and torques."""

    def __init__(self, posX, posY, mass, area, sailor):
        # Static properties
        self.mass = mass
        self.sailArea = area
        self.hullArea = 10 # arbitrary

        self.FORCE_CONST_AIR = 0.5 * DENSITY_AIR * self.sailArea # kg / m
        self.FORCE_CONST_WATER = 0.5 * DENSITY_WATER * self.hullArea # kg / m

        # Dynamic properties
        self.posX = posX
        self.posY = posY

        self.speedX = 0
        self.speedY = 0
        self.leewayAngle = 0

        self.sailor = sailor # Sail algorithm
        self.mainSailAngle = 0


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
        (apparentWindNormX, apparentWindNormY) = (apparentWindX / apparentWindSpeed, apparentWindY / apparentWindSpeed) # normalised apparent wind vector
        (speedNormX, speedNormY) = (self.speedX / boatSpeed, self.speedY / boatSpeed) # normalised speed vector

        leewayAngle = self.calcLeewayAngle()
        angleOfAttack = self.angleOfAttack(apparentWindAngle)

        # Sum up all acting forces
        # FIXME check if this can be implemented nicer
        sumX, sumY = 0, 0
        (forceX, forceY) = self.sailDrag(apparentWindNormX, apparentWindNormY, apparentWindSpeedSq, angleOfAttack)
        sumX += forceX
        sumY += forceY
        (forceX, forceY) = self.sailLift(apparentWindNormX, apparentWindNormY, apparentWindSpeedSq, apparentWindAngle, angleOfAttack)
        sumX += forceX
        sumY += forceY

        (forceX, forceY) = self.waterDrag(speedNormX, speedNormY, boatSpeedSq, leewayAngle)
        sumX += forceX
        sumY += forceY
        (forceX, forceY) = self.waterLift(speedNormX, speedNormY, boatSpeedSq, leewayAngle, apparentWindAngle)
        sumX += forceX
        sumY += forceY

        return (sumX, sumY)

    def sailDrag(self, apparentWindNormX, apparentWindNormY, apparentWindSpeedSq, angleOfAttack):
        """Calculate the force that is created when wind blows against the boat."""
        force = self.FORCE_CONST_AIR * apparentWindSpeedSq * sin(angleOfAttack) * self.coefficientAirDrag(angleOfAttack)
        return (force * apparentWindNormX, force * apparentWindNormY)

    def sailLift(self, apparentWindNormX, apparentWindNormY, apparentWindSpeedSq, apparentWindAngle, angleOfAttack):
        """Calculate the lift force that is created when the wind changes its direction in the sail."""
        force = self.FORCE_CONST_AIR * apparentWindSpeedSq * sin(angleOfAttack) * self.coefficientAirLift(angleOfAttack)
        if apparentWindAngle > 0: # NOTE potential error
            return (-force * apparentWindNormY, force * apparentWindNormX)  # rotate by -90°
        return (force * apparentWindNormY, -force * apparentWindNormX)      # rotate by  90°

    def waterDrag(self, speedNormX, speedNormY, boatSpeedSq, leewayAngle):
        """Calculate the drag force of the water that is decelerating the boat."""
        force = self.FORCE_CONST_WATER * boatSpeedSq * sin(leewayAngle) * self.coefficientWaterDrag(leewayAngle)
        return (-force * speedNormX, -force * speedNormY) # TODO waterDrag

    def waterLift(self, speedNormX, speedNormY, boatSpeedSq, leewayAngle, apparentWindAngle):
        """Calculate force that is caused by lift forces in the water."""
        force = self.FORCE_CONST_WATER * boatSpeedSq * sin(leewayAngle) * self.coefficientWaterLift(leewayAngle)
        if apparentWindAngle > 0: # NOTE potential error
            return (-force * speedNormY, force * speedNormX)    # rotate by  90°
        return (force * speedNormY, -force * speedNormX)        # rotate by -90°


    # Coefficient calculations
    def coefficientAirDrag(self, angleOfAttack):
        """Calculate the wind resitance coefficient based on the angle of attack."""
        # NOTE function has been approximated!
        # TODO calculate coefficient using Xfoil
        return 0.41 * pow(angleOfAttack, 2) + 0.13 * abs(angleOfAttack)

    def coefficientAirLift(self, angleOfAttack):
        """Calculate the wind lift coefficient based on the angle of attack."""
        # NOTE function has been approximated!
        # TODO calculate coefficient using Xfoil
        if abs(angleOfAttack) < 1.07:
            return 1.67
        return 11 * pow(angleOfAttack, 4) + 22.46 * pow(abs(angleOfAttack), 3) + 7.39 * pow(angleOfAttack, 2) + 5.88 * abs(angleOfAttack)

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
        return pow(apparentWindX, 2) + pow(apparentWindY, 2) # TODO stay in (-pi;pi] => %(2*pi)


    # Angle calculations
    def calcLeewayAngle(self):
        """Calculate and return the leeway angle."""
        # TODO exact calculation
        return 3

    def apparentWind(self, trueWindX, trueWindY):
        """Return apparent wind by adding true wind and speed."""
        return (trueWindX - self.speedX, trueWindY - self.speedY) # TODO stay in (-pi;pi] => %(2*pi)

    def apparentWindAngle(self, apparentWindX, apparentWindY):
        """Calculate the apparent wind angle based on the carthesian true wind."""
        return cartToArg(apparentWindX, apparentWindY) - cartToArg(self.speedX, self.speedY) # TODO stay in (-pi;pi] => %(2*pi)

    def angleOfAttack(self, apparentWindAngle): # TODO angleOfAttack oder vielleicht Segeleinstellung? Zusammenhang mit apparentWindAngle und Abdrift?
        """Calculate angle between main sail and apparent wind vector."""
        return pi - apparentWindAngle - self.mainSailAngle - self.leewayAngle # TODO stay in (-pi;pi] => %(2*pi)


    def __repr__(self):
        return "Boat @(%s|%s)\nv=%sm/s twds %s°" % (self.posX, self.posY, round(sqrt(self.boatSpeedSq()),2), round(cartToArg(self.speedX, self.speedY) * 360 / pi, 2))
