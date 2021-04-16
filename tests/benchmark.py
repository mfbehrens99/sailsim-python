# Import basic modules
from sailsim.simulation.Simulation import Simulation
from sailsim.world.World import World
from sailsim.boat.Boat import Boat
from sailsim.sailor.Sailor import Sailor
from sailsim.sailor.Commands import commandListExample

# Import Winds
from sailsim.wind.Wind import Wind
from sailsim.wind.Windfield import Windfield
from sailsim.wind.Fluctuationfield import Fluctuationfield


class Benchmark:
    """Test which module requires what partion of time when simulating."""

    def __init__(self):
        windfield = Windfield(0, 10)
        flucfield = Fluctuationfield(2, 10, 10, 0, 0, 1200)
        wind = Wind([windfield, flucfield])

        self.b = Boat(0, 0, 0)
        self.b.setMainSailAngleDeg(45)

        sailor = Sailor(commandListExample)
        sailor.importBoat(self.b)
        self.b.sailor = sailor

        w = World(self.b, wind, None)
        self.s = Simulation(w, 0.01)
        self.s.step()

    def run(self, number=10000):
        for i in range(number):
            self.s.step()
        self.s.frameList.saveCSV("simulation")
        self.b.sailor.frameList.saveCSV("sailor")


if __name__ == "__main__":
    import cProfile
    b = Benchmark()
    cProfile.run("b.run()", sort="cumtime", filename="test.profile")
