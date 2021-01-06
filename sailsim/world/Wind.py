import math

from sailsim.world.windfield import Windfield

class Wind:
    """Generates and calculates speed and direction of wind"""

    def __init__(self, sizeX, sizeY, winds):
        # TODO Size unnecessary?
        self.sizeX = sizeX
        self.sizeY = sizeY

        self.winds = winds

    def getWind(self, x, y):
        """Summs and returns the speed and direction of all windfields"""
        sumX = 0
        sumX = 0
        for wind in self.winds:
            (windX, windY) = wind.getWindCart(x, y)
            sumX += windX
            sumY += windY

        # Convert to polar
        speed = math.sqrt(sumX**2 + sumX**2)
        direction = (math.degrees(math.atan(sumY/sumX)) if sumX != 0 else (90 if sumY >= 0 else 270)) #TODO check
        return (speed, direction)
