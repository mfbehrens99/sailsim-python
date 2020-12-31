from simulation import Simulation

from world import World
from world import Boat
from world import Wind
from world import Windfield

from algorithmus import Algorithmus

def mainTest():
    boat = Boat()
    wf = Windfield(1, 0.5)
    wind = Wind(wf)

    world = World(boat,wind)

    sim = Simulation(.1, world)

    sim.runStep()
