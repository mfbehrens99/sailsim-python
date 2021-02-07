"""This is a basic simulation program. It is intended to serve as a basis for testing with a know output."""

# Import basic modules
from sailsim.simulation.Simulation import Simulation
from sailsim.world.World import World
from sailsim.world.Boat import Boat
from sailsim.world.Wind import Wind

# Import Winds
from sailsim.world.Windfield import Windfield
from sailsim.world.Squallfield import Squallfield

wf = Windfield(0, 10)
sqf = Squallfield(0, 0, 100, 1, 0) # TODO has to be enabled later

wind = Wind([wf, sqf])
b = Boat(0, 0, 100, 10, None)

b.speedX = 0
b.speedY = 1

# Create world and simulation
w = World(b, wind, None)
s = Simulation(w, 0.01, 256)

# Simulate 2 steps with print
print(s)
s.step()
print(s)
s.step()
print(s)

# Finish simulation
s.run()
print(s)
