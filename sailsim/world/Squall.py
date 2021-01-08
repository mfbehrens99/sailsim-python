from math import sin, cos

from sailsim.utils.coordconversion import cartToArg
from sailsim.world.Windfield import Windfield

class Squall(Windfield):
    """Holds all informationabout squalls"""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.maxsize = 1
        #TODO calc for maxsize

    def getWindCart(self, x, y):
        """Returns cartesian components of the windfield at the position (x,y) as a tuple"""
        windWeight = self.calcWindWeight(x, y)
        return (self.x * windWeight, self.y * windWeight)

    def calcWindWeight(self, x, y):
        """Return a factor for the strength of the wind depending on the form of the squall"""
        #TODO discuss if that is really worth the work
        (x, y) = self.rotatePosition(x, y)
        if -1 < x < 2 and abs(y) <.5:
            windWeight = self.windSquallFunction(x, y)
            if windWeight > 0:
                return windWeight
        return 0

    @staticmethod
    def windSquallFunction(x, y):
        """Static function that representates weight of the squall"""
        return .25*y**3-.75*y**2 - 2*x**2 + 1

    def rotatePosition(self,x,y):
        """Rotates position around center of squall as if squall was rotated"""
        direction = cartToArg(self.x, self.y)
        # A visualation of this calculation can be found in the docs foulder
        # less calculations, saves time
        sinDirection = sin(direction)
        cosDirection = cos(direction)
        rotX = x * cosDirection - y * sinDirection
        rotY = x * sinDirection + y * cosDirection
        return (rotX, rotY)
