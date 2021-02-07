"""This is a basic simulation program. It is intended to serve as a basis for testing with a know output."""

# Import basic modules
from sailsim.simulation.Simulation import Simulation
from sailsim.world.World import World
from sailsim.boat.Boat import Boat
from sailsim.wind.Wind import Wind

# Import Winds
from sailsim.wind.Windfield import Windfield
from sailsim.wind.Squallfield import Squallfield

wf = Windfield(10, 0)
sqf = Squallfield(0, 0, 100, 1, 0) # TODO has to be enabled later

wind = Wind([wf, sqf])
b = Boat(0, 0, 100, 10, None)

# Create world and simulation
w = World(b, wind, None)
s = Simulation(w, 0.01, 2048)

# Simulate 2 steps with print
print(s)
s.step()
print(s)
s.step()
print(s)

# Finish simulation
s.run()
print(s)
