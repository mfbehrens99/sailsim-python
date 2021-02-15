from random import getrandbits
from opensimplex import OpenSimplex # Noise function

from sailsim.wind.Windfield import Windfield
from sailsim.wind.Squall import Squall


class Squallfield(Windfield):
    """Simulate a field of squalls."""

    def __init__(self, x, y, gridDistance, displacementFactor=1, noiseSeed=0):
        """
        Create a Squallfield.

        Args:
            x:                  x component of wind in squall
            y:                  y component of wind in squall
            gridDistance:       theoretical distance between squalls
            displacementFactor: displacement of squalls in gridDistance, Note: will be scaled down by 0.8 due to simplex noise, default: 1
            noiseSeed:          seed for seedX, seedY = seedX + 1, default: random number [0; 2^32]
        """
        super().__init__(x, y)
        self.name = "Squallfield"

        self.squall = Squall(x, y)

        # Squall properties
        self.gridDistance = gridDistance
        self.displacementFactor = displacementFactor

        # Noise object creation
        self.noiseSeed = noiseSeed
        self.noiseX = OpenSimplex(noiseSeed)
        self.noiseY = OpenSimplex(noiseSeed + 1)

    def getWindCart(self, x, y, t):
        """Return cartesian components of the windfield at the position (x,y) as a tuple."""
        # Transform position instead of whole squall field
        (x, y) = self.transformPositionTime(x, y, t)

        (closestX, closestY) = self.closestPointIndex(x, y)

        # Iterate all relevant squalls
        # TODO Check if algorithm is not doing too much work
        sumX, sumY = 0, 0
        for itX in range(closestX - self.squall.maxsize, closestX + self.squall.maxsize + 1):
            for itY in range(closestY - self.squall.maxsize, closestY + self.squall.maxsize + 1):
                (relX, relY) = self.relativePosSquall(x, y, itX, itY)
                (windX, windY) = self.squall.getWindCart(relX, relY)
                sumX += windX
                sumY += windY

        return (sumX, sumY)

    def closestPointIndex(self, x, y):
        """Return the index of the closest points around the position x,y."""
        indexX = round(x / self.gridDistance)
        indexY = round(y / self.gridDistance)
        return(indexX, indexY)

    def displacePoint(self, x, y):
        """Pseudo randomly displaces point of a squall in x and y direction."""
        positionX = x * self.gridDistance + self.noiseX.noise2d(x, y) * self.displacementFactor
        positionY = y * self.gridDistance + self.noiseY.noise2d(x, y) * self.displacementFactor
        return (positionX, positionY)

    def relativePosSquall(self, x, y, indexX, indexY):
        """Calculate relative position to squall center."""
        relX = x - indexX * self.gridDistance
        relY = y - indexY * self.gridDistance
        return(relX, relY)

    def transformPositionTime(self, x, y, t):
        """Transform position based on speed and point in time (easier than to move the whole windfield)."""
        x -= self.speedX * t
        y -= self.speedY * t
        return (x, y)
