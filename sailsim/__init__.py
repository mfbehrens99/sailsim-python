from simulation import Simulation

from world.World import World
from world.Boat import Boat
from world.Wind import Wind
from world.Windfield import Windfield

from algorithmus import Algorithmus

def mainTest():
    boat = world.Boat()
    wf = world.Windfield(1, 0.5)
    wind = Wind.Wind(wf)

    w = world.World(boat,wind)

    sim = Simulation(.1, w)

    sim.runStep()
