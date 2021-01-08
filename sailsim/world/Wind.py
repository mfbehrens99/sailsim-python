from sailsim.utils.coordconversion import cartToPolar

from sailsim.world.Squallfield import Squallfield
from sailsim.world.Windfield import Windfield

class Wind:
    """Generates and calculates speed and direction of wind"""

    def __init__(self, winds):
        self.winds = winds

    def getWindCart(self, x, y, t):
        """Summs and returns the speed and direction of all windfields"""
        sumX = 0
        sumY = 0
        for wind in self.winds:
            (windX, windY) = wind.getWindCart(x, y, t)
            sumX += windX
            sumY += windY
        return (sumX, sumY)

    def getWind(self, x, y, t):
        """Returns direction and speed of the windfield at the position (x,y) as a tuple"""
        (cartX, cartY) = self.getWindCart(x, y, t)
        return cartToPolar(cartX, cartY)


    def __repr__(self):
        #TODO make nicer
        windfields = sum(isinstance(x, Windfield) for x in self.winds)
        squallfields = sum(isinstance(x, Squallfield) for x in self.winds)
        ret  = "Wind made up of " + str(len(self.winds)) + " winds:\n"
        ret += "\t" + str(windfields) + " Windfields\n"
        ret += "\t" + str(squallfields) + " Squallfield\n"
        return ret
