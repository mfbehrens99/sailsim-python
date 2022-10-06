"""Tests module sailsim.Simulation.Simulation (and many more)."""

from sailsim.simulation.Simulation import Simulation
from sailsim.boat.Boat import Boat
from sailsim.sailor.Sailor import Sailor
from sailsim.wind.Wind import Wind
from sailsim.wind.Windfield import Windfield


class TestSimulation():
    simulation: Simulation

    def setup(self) -> None:
        b = Boat()
        b.sailor = Sailor([])
        b.sailor.importBoat(b)
        self.simulation = Simulation(b, Wind([Windfield(0, 1)]), 0.01, 1)

    def test_step(self) -> None:
        self.simulation.step()

    def test_reset(self) -> None:
        self.simulation.reset()
        assert len(self.simulation.boat.frameList) == 0
        assert self.simulation.frame == 0

    def test_run(self) -> None:
        self.simulation.run()
        assert len(self.simulation.boat.frameList) == self.simulation.lastFrame + 1
        assert self.simulation.frame == self.simulation.lastFrame + 1
