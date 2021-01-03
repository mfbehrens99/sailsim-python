from sailsim.simulation.simulation import Simulation

from sailsim.world.world import World
from sailsim.world.boat import Boat
from sailsim.world.wind import Wind
from sailsim.world.windfield import Windfield

from sailsim.algorithmus import Algorithmus

if __name__ == '__main__':
    boat = Boat()
    wf = Windfield(1, 45)
    wind = Wind(20, 20, [wf])

    w = World(boat,wind,(52, 42))

    sim = Simulation(.1, w)

    sim.runStep()
