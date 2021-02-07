from random import getrandbits

from opensimplex import OpenSimplex # Noise function

from sailsim.wind.Windfield import Windfield

class Fluctuationfield(Windfield):
    def __init__(self, x, y, scale=1, speed=0, noiseSeed=None):
        super().__init__(x, y)

        self.scale = scale
        self.speed = speed

        if noiseSeed is None:
            noiseSeed = getrandbits(32)
        self.noiseX = OpenSimplex(noiseSeed)
        self.noiseY = OpenSimplex(noiseSeed + 1)
        self.noiseSeed = noiseSeed

    def getWindCart(self, x, y, t):
        """Return cartesian components of the windfield at the position (x,y) as a tuple."""
        return (0, 0)
