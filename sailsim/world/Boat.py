class Boat:
    """Holds all information about the boat and calculates its speed, forces and torques"""

    def __init__(self, posX, posY, mass, area, hull):
        # Static properties
        self.mass = mass
        self.sailArea = area
        self.hullArea = hull

        # Dynamic properties
        self.posX = posX
        self.posY = posY

        self.speedX = 0
        self.speedY = 0
        self.boatDirection = 0

        self.mainSailAngle = 0

    # Wind calculations
    def trueWindAngle(self, trueWindDirection):
        return trueWindDirection - self.sailDirection

    def apparentWindAngle(self, trueWindAngle): # Scheinbarer Wind
        return trueWindAngle #TODO apparentWindDirection

    def apparentWindDirection(self, trueWindAngle):
        """Apparent wind as it can be measured on the boat with reference to north"""
        return self.apparentWindAngle(trueWindAngle) + self.sailDirection # actually not needed


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


    # Force calculations
    def resultingForce(self, trueWindX, trueWindY):
        """Adds up all reacting forces and returns them as a tuple"""
        apparentWindSpeed = trueWindSpeed #TODO apparentWindSpeed
        apparentWindAngle = self.apparentWindAngle(self.trueWindAngle(trueWindDirection))

        #TODO check if this can be implemented nicer
        sumX, sumY = 0, 0
        (forceX, forceY) = self.sailDrag(apparentWindAngle, apparentWindSpeed)
        sumX += forceX
        sumY += forceY
        (forceX, forceY) = self.sailLift(apparentWindAngle, apparentWindSpeed)
        sumX += forceX
        sumY += forceY

        # (forceX, forceY) = self.waterResistance()
        # sumX += forceX
        # sumY += forceY
        # (forceX, forceY) = self.waterLift()
        # sumX += forceX
        # sumY += forceY

        return (sumX, sumY)

    def sailDrag(self, apparentWindAngle, apparentWindSpeed):
        """Calculates the force that is created when wind blows against the boat"""
        return (0,0) #TODO sailResistance

    def sailLift(self, apparentWindAngle, apparentWindSpeed):
        """Calculates the lift force that is created when the wind changes its direction in the sail"""
        return (0,0) #TODO sailLift

    def waterResistance(self):
        """Calculates the restance force of the water that is decelerating the boat"""
        return (0,0) #TODO waterResistance

    def waterLift(self):
        return (0,0) #TODO waterLift
