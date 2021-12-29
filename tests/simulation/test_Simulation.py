"""Tests module sailsim.Simulation.Simulation (and many more)."""

from sailsim.simulation.Simulation import Simulation
from sailsim.boat.Boat import Boat
from sailsim.wind.Wind import Wind
from sailsim.wind.Windfield import Windfield


class TestSimulation():
    def setup(self):
        self.s = Simulation(Boat(), Wind([Windfield(0, 1)]), 0.01, 1)

    def test_step(self):
        self.s.step()

    def test_reset(self):
        self.s.reset()
        assert len(self.s.boat.frameList) == 0
        assert self.s.frame == 0

    def test_run(self):
        self.s.run()
        assert len(self.s.boat.frameList) == self.s.lastFrame + 1
        assert self.s.frame == self.s.lastFrame + 1
