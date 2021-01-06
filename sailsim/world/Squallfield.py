from random import getrandbits

from opensimplex import OpenSimplex # Noise function

from sailsim.world.windfield import Windfield
from sailsim.world.squall import Squall

class Squallfield(Windfield):
    """Simulates a field of squalls"""
    def __init__(self, x, y, gridDistance, displacementFactor = 1, noiseSeed = None):
        super().__init__(x, y)

        self.squall = Squall(x, y)

        # Squall properties
        self.gridDistance = gridDistance
        self.displacementFactor = displacementFactor

        # Noise object creation
        # Apply random seed if no seed is provided
        if noiseSeed is None:
            noiseSeed = getrandbits(32) # Just a random time efficent algorithm
        self.noiseX = OpenSimplex(noiseSeed)
        self.noiseY = OpenSimplex(noiseSeed + 1)
        self.noiseSeed = noiseSeed

    def getWindCart(self, x, y, t):
        """Returns cartesian components of the windfield at the position (x,y) as a tuple"""
        # Transform position instead of whole squall field
        (x, y) = self.transformPositionTime(x, y, t)

        (closestX, closestY) = self.closestPointIndex(x, y)

        # Iterate all relevant squalls
        #TODO Check if algorithm is not doing too much work
        sumX, sumY = 0, 0
        for itX in range(closestX - self.squall.maxsize, closestX + self.squall.maxsize + 1):
            for itY in range(closestY - self.squall.maxsize, closestY + self.squall.maxsize + 1):
                (relX, relY) = self.relativePosSquall(x, y, itX, itY)
                (windX, windY) = self.squall.getWindCart(relX, relY)
                sumX += windX
                sumY += windY

        return (sumX, sumY)

    def closestPointIndex(self, x, y):
        """Returns the index of the closest points around the position x,y"""
        indexX = round(x/self.gridDistance)
        indexY = round(y/self.gridDistance)
        return(indexX, indexY)

    def displacePoint(self, x, y):
        """Pseudo randomly displaces point of a squall in x and y direction"""
        # Bitshift for scaling the noise so it is 'more' random
        positionX = x * self.gridDistance + self.noiseX.noise2d(x<<4, y<<4) * self.displacementFactor
        positionY = y * self.gridDistance + self.noiseY.noise2d(x<<4, y<<4) * self.displacementFactor
        return (positionX, positionY)

    def relativePosSquall(self, x, y, indexX, indexY):
        """Calculates relative position to squall center"""
        relX = x - indexX * self.gridDistance
        relY = y - indexY * self.gridDistance
        return(relX, relY)

    def transformPositionTime(self, x, y, t):
        """Transforms position based on speed and point in time (easier than to move the whole windfield)"""
        x -= self.x * t
        y -= self.y * t
        return (x, y)
