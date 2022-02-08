# Import basic modules
from sailsim.simulation.Simulation import Simulation
from sailsim.boat.Boat import Boat
from sailsim.sailor.Sailor import Sailor
from sailsim.sailor.Commands import commandListExample

# Import Winds
from sailsim.wind.Windfield import Windfield


OUTPUT_PATH = "test"

class Benchmark:
    """Test which module requires what partion of time when simulating."""

    def __init__(self):
        wind = Windfield(2, 2)
        boat = Boat(0, 0, 0)
        sailor = Sailor(commandListExample)
        boat.sailor = sailor
        sailor.importBoat(boat)

        self.simulation = Simulation(boat, wind, 0.01, 1000)


    def run(self, number=10000):
        self.simulation.run(number)
        # self.simulation.frameList.saveCSV(OUTPUT_PATH)


if __name__ == "__main__":
    import cProfile
    b = Benchmark()
    cProfile.run("b.run()", 'out.prof', sort="cumtime")
