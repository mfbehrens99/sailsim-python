from opensimplex import OpenSimplex # Noise function

from sailsim.wind.Windfield import Windfield


class Fluctuationfield(Windfield):
    """Field that is usually added on top of a windfield to create pseudo random fluctuations."""

    def __init__(self, x=0, y=0, amplitude=1, scale=64, speed=16, noiseSeed=0):
        """
        Create a Fluctuationfield.

        Parameters:
         - x:           constant wind in x direction, default: 0 m/s
         - y:           constant wind in y direction, default: 0 m/s
         - amplitude:   scaling of the noise output. Note: output is in range ~[-0.8; 0.8], default: +-1 m/s => +-0.8 m/s
         - scale:       theoretical distance (in meters) between min and max of the fluctuations, default: 64 m
         - speed:       theoretical time (in seconds) it takes from min to max, default: 16 s
         - noiseSeed:   seed for seedX, seedY = seedX + 1, default: 0
        """
        super().__init__(x, y)

        self.amplitude = amplitude
        self.scale = self.speed = None
        self.setScale(scale)
        self.setSpeed(speed)

        self.noiseSeed = noiseSeed
        self.noiseX = OpenSimplex(noiseSeed)
        self.noiseY = OpenSimplex(noiseSeed + 1)

    def getWindCart(self, x, y, t):
        """Return cartesian components of the windfield at the position (x,y) as a tuple."""
        windX = self.noiseX.noise3(x * self.scale, y * self.scale, t * self.speed) * self.amplitude + self.speedX
        windY = self.noiseY.noise3(x * self.scale, y * self.scale, t * self.speed) * self.amplitude + self.speedY
        return (windX, windY)

    def setScale(self, scale):
        self.scale = 1 / scale

    def setSpeed(self, speed):
        self.speed = 1 / (speed * 2)

    def getScale(self):
        return 1 / self.scale

    def getSpeed(self):
        return 1 / (self.speed * 2)
