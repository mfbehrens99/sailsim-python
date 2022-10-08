"""This is a basic simulation program. It is intended to serve as a basis for testing with a know output."""

# Import modules
from numpy import array
import numpy as np

# Import gui
import sys
from PySide6.QtWidgets import QApplication
from sailsim.gui.SailsimGUI import SailsimGUI

# Import basic modules
from sailsim.simulation.Simulation import Simulation
from sailsim.boat.Boat import Boat
from sailsim.sailor.Sailor import Sailor
from sailsim.sailor.Commands import commandListExample, Waypoint
from sailsim.wind.Fluctuationfield import Fluctuationfield

# Define Wind
wind = Fluctuationfield(0, 10, 1)

# Create and configure boat and sailor
sailor = Sailor(commandListExample)
#sailor = Sailor([Waypoint(-30, 30, 1), Waypoint(10, 47, 1), Waypoint(100, 60, 1), Waypoint(0, 100, 2)])

b = Boat()
b.sailor = sailor

sailor.importBoat(b)

# Create simulation
s = Simulation(b, wind, 0.01, 1000)

# Run simulation
try:
    s.run()
except (OverflowError, ValueError):
    s.lastFrame = s.frame - 1
    print("Overflow after Frame", s.frame)

#OUTPUT_PATH = "..\\..\\MATLAB\\sailsim\\out.csv"
#s.boat.frameList.saveCSV(OUTPUT_PATH)

app = QApplication(sys.argv)
window = SailsimGUI(s)
window.show()
sys.exit(app.exec())
