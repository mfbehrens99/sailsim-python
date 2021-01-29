from math import sin, sqrt, pi

from sailsim.utils.constants import DENSITY_AIR
from sailsim.utils.coordconversion import cartToArg

class Boat:
    """Holds all information about the boat and calculates its speed, forces and torques"""

    def __init__(self, posX, posY, mass, area, sailor):
        # Static properties
        self.mass = mass
        self.sailArea = area
        self.FORCE_CONST_AIR = 0.5 * DENSITY_AIR * self.sailArea # kg / m

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
        """Changes speed according a force given"""
        # △v = a * t ; F = m * a
        # △v = F / m * t
        self.speedX += forceX / self.mass * interval
        self.speedY += forceY / self.mass * interval

    def moveInterval(self, interval):
        """Changes position according to sailsDirection and speed"""
        # s = v * t
        self.posX += self.speedX * interval
        self.posY += self.speedY * interval

    def runSailor(self):
        """Activates the sailing algorithm to decide what the boat should do"""
        pass


    # Force calculations
    def resultingForce(self, trueWindX, trueWindY):
        """Adds up all reacting forces and returns them as a tuple"""
        (apparentWindX, apparentWindY) = self.apparentWind(trueWindX, trueWindY)

        apparentWindAngle = self.apparentWindAngle(apparentWindX, apparentWindY)
        apparentWindSpeedSq = self.apparentWindSpeedSq(apparentWindX, apparentWindY)

        apparentWindSpeed = sqrt(apparentWindSpeedSq)
        (apparentWindNormX, apparentWindNormY) = (apparentWindX / apparentWindSpeed, apparentWindY / apparentWindSpeed)

        #TODO calculate leewayAngle
        angleOfAttack = self.angleOfAttack(apparentWindAngle)

        #FIXME check if this can be implemented nicer
        sumX, sumY = 0, 0
        (forceX, forceY) = self.sailDrag(apparentWindNormX, apparentWindNormY, apparentWindSpeedSq, angleOfAttack)
        sumX += forceX
        sumY += forceY
        (forceX, forceY) = self.sailLift(apparentWindNormX, apparentWindNormY, apparentWindSpeedSq, apparentWindAngle, angleOfAttack)
        sumX += forceX
        sumY += forceY

        # (forceX, forceY) = self.waterResistance()
        # sumX += forceX
        # sumY += forceY
        # (forceX, forceY) = self.waterLift()
        # sumX += forceX
        # sumY += forceY

        return (sumX, sumY)

    def sailDrag(self, apparentWindNormX, apparentWindNormY, apparentWindSpeedSq, angleOfAttack):
        """Calculates the force that is created when wind blows against the boat"""
        force = self.FORCE_CONST_AIR * apparentWindSpeedSq * sin(angleOfAttack) * self.coefficientDrag(angleOfAttack)
        return (force * apparentWindNormX, force * apparentWindNormY)

    def sailLift(self, apparentWindNormX, apparentWindNormY, apparentWindSpeedSq, apparentWindAngle, angleOfAttack):
        """Calculates the lift force that is created when the wind changes its direction in the sail"""
        force = self.FORCE_CONST_AIR * apparentWindSpeedSq * sin(angleOfAttack) * self.coefficientLift(angleOfAttack)
        if apparentWindAngle > 0: #NOTE potetial error
            return (-force * apparentWindNormY, force * apparentWindNormX) # rotate by -90°
        else:
            return (force * apparentWindNormY, -force * apparentWindNormX) # rotate by  90°

    def waterResistance(self):
        """Calculates the restance force of the water that is decelerating the boat"""
        return (0,0) #TODO waterResistance

    def waterLift(self):
        return (0,0) #TODO waterLift


    # Coefficient calculations
    def coefficientDrag(self, angleOfAttack):
        return 0

    def coefficientLift(self, angleOfAttack):
        return 0 #TODO Xfoil


    # Angle calculations
    def calcLeewayAngle(self):
        pass

    def apparentWind(self, trueWindX, trueWindY):
        return (trueWindX - self.speedX, trueWindY - self.speedY)

    def apparentWindAngle(self, apparentWindX, apparentWindY):
        """Calculates the apparent wind angle based on the carthesian true wind"""
        return cartToArg(apparentWindX, apparentWindY) - cartToArg(self.speedX, self.speedY) #TODO %(2*pi) ???

    def apparentWindSpeedSq(self, apparentWindX, apparentWindY):
        return pow(apparentWindX, 2) + pow(apparentWindY, 2)

    def angleOfAttack(self, apparentWindAngle):
        return pi - apparentWindAngle - self.mainSailAngle - self.leewayAngle  #TODO angleOfAttack oder vielleicht Segeleinstellung? Zusammenhang mit apparentWindAngle und Abdrift?
