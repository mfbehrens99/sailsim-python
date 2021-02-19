# Import basic modules
from sailsim.simulation.Simulation import Simulation
from sailsim.world.World import World
from sailsim.boat.Boat import Boat
from sailsim.wind.Wind import Wind

# Import Winds
from sailsim.wind.Windfield import Windfield
from sailsim.wind.Fluctuationfield import Fluctuationfield
from sailsim.wind.Squallfield import Squallfield


OUTPUT_PATH = "test"

class Benchmark:
    """Test which module requires what partion of time when simulating."""

    def __init__(self):
        windfield = Windfield(0, 10)
        flucfield = Fluctuationfield(2, 10, 10, 0, 0, 1200)
        squallfield = Squallfield(0, 0, 100, 1, 0) # TODO has to be enabled later
        wind = Wind([windfield, flucfield, squallfield])

        b = Boat(0, 0, 0)
        b.setMainSailAngleDeg(45)

        w = World(b, wind, None)
        self.s = Simulation(w, 0.01, 1024)

    def run(self, number=10000):
        for i in range(number):
            self.s.step()
        self.s.frameList.saveCSV(OUTPUT_PATH)


if __name__ == "__main__":
    import cProfile
    b = Benchmark()
    cProfile.run("b.run()", sort="cumtime")
