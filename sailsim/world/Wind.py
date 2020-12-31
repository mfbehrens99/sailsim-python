from world import Windfield

class Wind:
    """Generates and calculates speed and direction of wind"""

    def __init__(self, sizeX, sizeY, winds):
        # Size unnecessary?
        self.sizeX = sizeX
        self.sizeY = sizeY

        self.winds = winds

    def getWind(x, y):
        # work with wind as a vector with x,y component rather than polar coordinates?
        speed, direction
        for wind in winds:
            wind.getWind(x,y)
            # TODO addition of winds
        return (speed, direction)
