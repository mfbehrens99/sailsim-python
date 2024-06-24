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
from sailsim.wind.Fluctuationfield import Fluctuationfield

# Define Wind
wind = Fluctuationfield(0, 10, 1)

# Create and configure boat and sailor
sailor = Sailor(commandListExample)
#sailor = Sailor([Waypoint(-30, 30, 1), Waypoint(10, 47, 1), Waypoint(100, 60, 1), Waypoint(0, 100, 2)])

boat = Boat(0, 0, 0)
boat.sailor = sailor

sailor.importBoat(boat)

# Create simulation
simulation = Simulation(boat, wind, 0.01, 10000)

# Run simulation
try:
    simulation.run()
except (OverflowError, ValueError):
    simulation.lastFrame = simulation.frame - 1
    print("Overflow after Frame", simulation.frame)

#OUTPUT_PATH = "..\\..\\MATLAB\\sailsim\\out.csv"
#s.boat.frameList.saveCSV(OUTPUT_PATH)

app = QApplication(sys.argv)
window = SailsimGUI(simulation, locals())
window.show()
sys.exit(app.exec())
