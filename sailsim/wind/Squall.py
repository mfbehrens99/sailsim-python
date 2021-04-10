from math import sin, cos

from sailsim.utils.coordconversion import cartToArg
from sailsim.wind.Windfield import Windfield


class Squall(Windfield):
    """Hold all information about squalls in a squallfield."""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Squall"
        self.maxsize = 1
        # TODO calc for maxsize

    def getWindCart(self, x, y):
        """Return cartesian components of the windfield at the position (x,y) as a tuple."""
        windWeight = self.calcWindWeight(x, y)
        return (self.speedX * windWeight, self.speedY * windWeight)

    def calcWindWeight(self, x, y):
        """Return a factor for the strength of the wind depending on the form of the squall."""
        # TODO discuss if that is really worth the work
        (x, y) = self.rotatePosition(x, y)
        if -1 < x < 2 and abs(y) < .5:
            windWeight = self.windSquallFunction(x, y)
            if windWeight > 0:
                return windWeight
        return 0

    @staticmethod
    def windSquallFunction(x, y):
        """Return weight of the squall at position x, y."""
        return .25 * y**3 - .75 * y**2 - 2 * x**2 + 1

    def rotatePosition(self, x, y):
        """Rotate position around center of squall as if squall was rotated."""
        direction = cartToArg(self.speedX, self.speedY)
        # A visualation of this calculation can be found in the docs foulder
        # less calculations, saves time
        sinDirection = sin(direction)
        cosDirection = cos(direction)
        rotX = x * cosDirection - y * sinDirection
        rotY = x * sinDirection + y * cosDirection
        return (rotX, rotY)
