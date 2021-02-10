from random import getrandbits
from opensimplex import OpenSimplex # Noise function

from sailsim.wind.Windfield import Windfield


class Fluctuationfield(Windfield):
    """Field that is usually added on top of a windfield to create pseudo random fluctuations."""

    def __init__(self, amplitude=1, scale=64, speed=16, x=0, y=0, noiseSeed=None):
        """
        Create a Fluctuationfield.

        Parameters:
         - amplitude:   scaling of the noise output. Note: output is in range ~[-0.8; 0.8], default: +-1 m/s => +-0.8 m/s
         - scale:       theoretical distance (in meters) between min and max of the fluctuations, default: 64 m
         - speed:       theoretical time (in seconds) it takes from min to max, default: 16 s
         - x:           constant wind in x direction, default: 0 m/s
         - y:           constant wind in y direction, default: 0 m/s
         - noiseSeed:   seed for seedX, seedY = seedX + 1, default: random number [0; 2^32]
        """
        super().__init__(x, y)

        self.amplitude = amplitude
        self.scale = 1 / scale
        self.speed = 1 / (speed * 2)

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
