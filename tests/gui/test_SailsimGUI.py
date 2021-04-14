"""Test module sailsim.gui.SailsimGUI."""

import sys
from PySide6.QtWidgets import QApplication
from sailsim.gui.SailsimGUI import SailsimGUI

from sailsim.simulation.Simulation import Simulation
from sailsim.world.World import World
from sailsim.boat.Boat import Boat
from sailsim.wind.Wind import Wind
from sailsim.wind.Windfield import Windfield


def test_main():
    world = World(Boat(), Wind([Windfield(0, 1)]), None)
    s = Simulation(world, 0.01, 1)

    app = QApplication(sys.argv)
    window = SailsimGUI(s)
    window.show()
    # sys.exit(app.exec_())
