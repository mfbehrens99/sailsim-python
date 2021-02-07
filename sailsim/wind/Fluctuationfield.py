from random import getrandbits

from opensimplex import OpenSimplex # Noise function

from sailsim.wind.Windfield import Windfield


class Fluctuationfield(Windfield):
    """Field that is usually added on top of a windfield to create pseudo random fluctuations."""

    def __init__(self, amplitude=1, scale=1, speed=0, x=0, y=0, noiseSeed=None):
        super().__init__(x, y)

        self.amplitude = amplitude
        self.scale = scale
        self.speed = speed

        self.speedX = x
        self.speedY = y

        if noiseSeed is None:
            noiseSeed = getrandbits(32)
        self.noiseX = OpenSimplex(noiseSeed)
        self.noiseY = OpenSimplex(noiseSeed + 1)
        self.noiseSeed = noiseSeed

    def getWindCart(self, x, y, t):
        """Return cartesian components of the windfield at the position (x,y) as a tuple."""
        windX = self.noiseX.noise3d(x * self.scale, y * self.scale, t * self.speed) * self.amplitude + self.speedX
        windY = self.noiseY.noise3d(x * self.scale, y * self.scale, t * self.speed) * self.amplitude + self.speedY
        return (windX, windY)
