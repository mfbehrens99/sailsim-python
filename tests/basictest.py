"""This is a basic simulation program. It is intended to serve as a basis for testing with a know output."""

# Import gui
import sys
from PySide6.QtWidgets import QApplication
from sailsim.gui.SailsimGUI import SailsimGUI

# Import basic modules
from sailsim.simulation.Simulation import Simulation
from sailsim.world.World import World
from sailsim.boat.Boat import Boat
from sailsim.sailor.Sailor import Sailor
from sailsim.sailor.Commands import commandListExample

# Import Winds
from sailsim.wind.Wind import Wind
from sailsim.wind.Windfield import Windfield
from sailsim.wind.Fluctuationfield import Fluctuationfield
from sailsim.wind.Squallfield import Squallfield

from sailsim.gui.ConfigWind import ConfigWind
from sailsim.gui.ConfigBoat import ConfigBoat

OUTPUT_PATH = "..\\..\\MATLAB\\sailsim\\out.csv"

# Define Wind
wf = Windfield(0, 10)
flctf = Fluctuationfield(1)
sqf = Squallfield(0, 0, 100, 1, 0) # TODO has to be enabled later
wind = Wind([wf, flctf, sqf])
ConfigWind(wind).mainloop()

# Create and configure boat and sailor
sailor = Sailor(commandListExample)

b = Boat(0, 0, 0)
b.setMainSailAngleDeg(0)
ConfigBoat(b, wind).mainloop()
b.sailor = sailor

sailor.importBoat(b)

# Create world and simulation
w = World(b, wind, None)
s = Simulation(w, 0.01, 1000)

# Run simulation
try:
    s.run()
except OverflowError:
    print("Overflow after Frame", s.frame)

app = QApplication(sys.argv)

window = SailsimGUI(s)
window.show()

sys.exit(app.exec_())

s.frameList.saveCSV(OUTPUT_PATH)
