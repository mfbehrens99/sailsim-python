from sailsim.utils.coordconversion import cartToPolar

from sailsim.wind.Windfield import Windfield
from sailsim.wind.Fluctuationfield import Fluctuationfield
from sailsim.wind.Squallfield import Squallfield


class Wind:
    """This class holds all windfields and calculates speed and direction of wind."""

    def __init__(self, winds):
        self.winds = winds

    def getWindCart(self, x, y, t):
        """Summ up and returns the speed and direction of all windfields."""
        sumX = 0
        sumY = 0
        for wind in self.winds:
            (windX, windY) = wind.getWindCart(x, y, t)
            sumX += windX
            sumY += windY
        return (sumX, sumY)

    def getWind(self, x, y, t):
        """Return direction and speed of the windfield at the position (x,y) as a tuple."""
        (cartX, cartY) = self.getWindCart(x, y, t)
        return cartToPolar(cartX, cartY)


    def __repr__(self):
        # TODO make nicer
        windfields = sum(isinstance(x, Windfield) for x in self.winds)
        fluctuationfields = sum(type(x) is Fluctuationfield for x in self.winds)
        squallfields = sum(type(x) is Squallfield for x in self.winds)
        return "Wind made up of %s winds:\n\t%s Windfields\n\t%s Fluctuationfields\n\t%s Squallfields" % (len(self.winds), windfields, fluctuationfields, squallfields)
