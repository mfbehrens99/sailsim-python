import math

from world import Windfield

class Wind:
    """Generates and calculates speed and direction of wind"""

    def __init__(self, sizeX, sizeY, winds):
        # TODO Size unnecessary?
        self.sizeX = sizeX
        self.sizeY = sizeY

        self.winds = winds

    def getWind(self, x, y):
        """Summs and returns the speed and direction of all windfields"""
        sum_x = 0
        sum_y = 0
        for wind in self.winds:
            (wind_x, wind_y) = wind.getWindCart(x, y)
            sum_x += wind_x
            sum_y += wind_y

        # Convert to polar
        speed = math.sqrt(sum_x**2 + sum_y**2)
        direction = (math.degrees(math.atan(sum_y/sum_x)) if sum_x != 0 else (90 if sum_y >= 0 else 270))
        return (speed, direction)
