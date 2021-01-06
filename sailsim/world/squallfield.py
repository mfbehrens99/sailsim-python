from random import random

from opensimplex import OpenSimplex #noise function

from sailsim.world.windfield import Windfield

class Squallfield(Windfield):
    """Simulates a field of squalls"""
    def __init__(self, speed, direction, gridDistance, displacementFactor, noiseSeed = None):
        super().__init__(speed, direction) #call normal windfield constructor

        self.gridDistance = gridDistance
        self.displacementFactor = displacementFactor

        if noiseSeed is None:
            noiseSeed = int(random.random()*2**16) #can be changed for something else
        self.noise = OpenSimplex(noiseSeed)

    def getWind(self,x,y,t):
        #TODO check which points are relevant
        pass

    def displacePoint(self):
        pass
