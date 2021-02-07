"""This is a basic simulation program. It is intended to serve as a basis for testing with a know output."""

# Import basic modules
from sailsim.simulation.Simulation import Simulation
from sailsim.world.World import World
from sailsim.world.Boat import Boat
from sailsim.world.Wind import Wind

# Import Winds
from sailsim.world.Windfield import Windfield
from sailsim.world.Squallfield import Squallfield

wf = Windfield(0, 0)
sqf = Squallfield(0, 0, 100, 1, 0)

wind = Wind([wf, sqf])
boat = Boat(0, 0, 100, 10, None)

w = World(boat, wind, None)

s = Simulation(w, 0.01, 2048)

s.run()
