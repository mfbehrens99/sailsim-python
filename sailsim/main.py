from simulation.simulation import Simulation

from world.world import World
from world.boat import Boat
from world.wind import Wind
from world.windfield import Windfield

#from algorithmus import Algorithmus

if __name__ == '__main__':
    boat = Boat()
    wf = Windfield(1, 45)
    wind = Wind(20, 20, [wf])

    w = World(boat,wind,(52, 42))

    sim = Simulation(.1, w)

    sim.runStep()
