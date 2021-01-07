from sailsim.world.Wind import Wind
from sailsim.world.Squallfield import Squallfield

#TODO this should test a simulation step

class Benchmark:
    def __init__(self):
        squallfield = Squallfield(3,2,2,1)
        self.wind = Wind([squallfield])

    def run(self, number=100000):
        for i in range(number):
            self.wind.getWind(0,0,i)

if __name__ == "__main__":
    import cProfile
    b = Benchmark()
    cProfile.run("b.run()", sort="tottime")
