"""This is a basic simulation program. It is intended to serve as a basis for testing with a know output."""

# Import basic modules
from sailsim.simulation.Simulation import Simulation
from sailsim.world.World import World
from sailsim.boat.Boat import Boat
from sailsim.wind.Wind import Wind

# Import Winds
from sailsim.wind.Windfield import Windfield
from sailsim.wind.Fluctuationfield import Fluctuationfield
from sailsim.wind.Squallfield import Squallfield

OUTPUT_PATH = "/to/output/path/basictest.csv"

wf = Windfield(0, 10)
flctf = Fluctuationfield(2, 10, 10, 0, 0, 1200)
sqf = Squallfield(0, 0, 100, 1, 0) # TODO has to be enabled later
wind = Wind([wf, flctf, sqf])
print(wind)

b = Boat(0, 0, 0)
b.setMainSailAngleDeg(45)

# Create world and simulation
w = World(b, wind, None)
s = Simulation(w, 0.01, 1024)

# Simulate 1 step
s.step()

# Finish simulation
s.run()
print(s)

s.frameList.saveCSV(OUTPUT_PATH)
