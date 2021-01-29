from sailsim.world.Wind import Wind

from sailsim.world.Windfield import Windfield
from sailsim.world.Squallfield import Squallfield


# TODO this should test a simulation step

class Benchmark:
    """Test which module requires what partion of time when simulating."""

    def __init__(self):
        windField = Windfield(3, 2)
        squallfield = Squallfield(3, 2, 2, 1)
        self.wind = Wind([windField, squallfield])

    def run(self, number=100000):
        for i in range(number):
            self.wind.getWind(0, 0, i)


if __name__ == "__main__":
    import cProfile
    b = Benchmark()
    cProfile.run("b.run()", sort="tottime")
