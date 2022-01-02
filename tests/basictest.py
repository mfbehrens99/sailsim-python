"""This is a basic simulation program. It is intended to serve as a basis for testing with a know output."""

# Import gui
import sys
from PySide6.QtWidgets import QApplication
from sailsim.gui.SailsimGUI import SailsimGUI

# Import basic modules
from sailsim.simulation.Simulation import Simulation
from sailsim.boat.Boat import Boat
from sailsim.sailor.Sailor import Sailor
from sailsim.sailor.Commands import commandListExample, Waypoint

# Import Winds
from sailsim.wind.Wind import Wind
from sailsim.wind.Windfield import Windfield
from sailsim.wind.Fluctuationfield import Fluctuationfield
from sailsim.wind.Squallfield import Squallfield

# Define Wind
wf = Windfield(0, 10)
flctf = Fluctuationfield(1)
sqf = Squallfield(0, 0, 100, 1, 0) # TODO has to be enabled later
wind = Wind([wf, flctf, sqf])

# Create and configure boat and sailor
sailor = Sailor(commandListExample)
#sailor = Sailor([Waypoint(-30, 30, 1), Waypoint(10, 47, 1), Waypoint(100, 60, 1), Waypoint(0, 100, 2)])

b = Boat(0, 0, 0)
b.sailor = sailor

sailor.importBoat(b)

# Create simulation
s = Simulation(b, wind, 0.01, 1000)

# Run simulation
try:
    s.run()
except OverflowError:
    s.lastFrame = s.frame - 1
    print("Overflow after Frame", s.frame)

#OUTPUT_PATH = "..\\..\\MATLAB\\sailsim\\out.csv"
#s.boat.frameList.saveCSV(OUTPUT_PATH)

app = QApplication(sys.argv)
window = SailsimGUI(s)
window.show()
sys.exit(app.exec())
