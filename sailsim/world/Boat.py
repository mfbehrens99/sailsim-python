class Boat:
    """Holds all information about the boat"""

    def __init__(self, position, mass, area, hull):
        self.position = position

        #static properties
        self.mass = mass
        self.sailarea = area
        self.hullarea = hull

        #dynamic properties
        self.speed = 0
        self.accel = 0
        self.boatDirection = 0
        self.sailDirection = 0

        self.mainSailAngle = 0

    # Wind calculations
    def trueWindAngle(self, trueWindDirection):
        return trueWindDirection - self.sailDirection

    def apparentWindAngle(self, trueWindAngle): # Scheinbarer Wind
        return trueWindAngle #TODO apparantWindDirection

    def apparentWindDirection(self, trueWindAngle): #Scheinbare Windrichtung in Bezug auf Norden
        return self.apparentWindAngle(trueWindAngle) + self.sailDirection # not needed very frequently


    # Force calculations
    def resultingForce(self,trueWindDirection):
        apparent_wind_angle = self.apparentWindAngle(self.trueWindAngle(trueWindDirection))

        force = (0,0)
        force += self.sailResistance(apparent_wind_angle)
        force += self.sailLift(apparent_wind_angle)

        force += self.waterResistance()
        force += self.waterLift()

        return force #TODO check if this is not produceing an error

    def sailResistance(self, apparentWindAngle):
        return (0,0) #TODO sailResistance

    def sailLift(self, apparentWindAngle):
        return (0,0) #TODO sailLift

    def waterResistance(self):
        return (0,0) #TODO waterResistance

    def waterLift(self):
        return (0,0) #TODO waterLift
