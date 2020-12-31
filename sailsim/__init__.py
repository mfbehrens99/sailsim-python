from simulation import Simulation
from world import World
from algorithmus import Algorithmus

def simulationTest():
    boat = Boat()
    wf = Windfield(1, 0.5)
    wind = Wind(wf)

    world = World(boat,wind)

    sim = Simulation(.1, world)

    sim.runStep()
