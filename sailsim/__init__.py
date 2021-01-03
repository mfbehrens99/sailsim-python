from simulation.Simulation import Simulation

from world.World import World
from world.Boat import Boat
from world.Wind import Wind
from world.Windfield import Windfield

from algorithmus import Algorithmus

if __name__ == '__main__':
    boat = Boat()
    wf = Windfield(1, 0.5)
    wind = Wind(20, 20, [wf])

    w = World(boat,wind,(52, 42))

    sim = Simulation(.1, w)

    sim.runStep()
