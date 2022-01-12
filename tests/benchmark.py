# Import basic modules
from sailsim.simulation.Simulation import Simulation
from sailsim.boat.Boat import Boat
from sailsim.sailor.Sailor import Sailor
from sailsim.sailor.Commands import commandListExample

# Import Winds
from sailsim.wind.Windfield import Windfield
from sailsim.wind.Fluctuationfield import Fluctuationfield
from sailsim.wind.Squallfield import Squallfield


OUTPUT_PATH = "test"

class Benchmark:
    """Test which module requires what partion of time when simulating."""

    def __init__(self):
        flucfield = Fluctuationfield(2, 10, 10, 0, 0, 1200)
        b = Boat(0, 0, 0)
        s = Sailor(commandListExample)
        b.sailor = s
        s.importBoat(b)

        self.s = Simulation(b, flucfield, 0.01, 1024)


    def run(self, number=10000):
        for i in range(number):
            self.s.step()
        #self.s.frameList.saveCSV(OUTPUT_PATH)


if __name__ == "__main__":
    import cProfile
    b = Benchmark()
    cProfile.run("b.run()", sort="cumtime")
