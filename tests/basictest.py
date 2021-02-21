"""This is a basic simulation program. It is intended to serve as a basis for testing with a know output."""

# Import basic modules
from sailsim.simulation.Simulation import Simulation
from sailsim.world.World import World
from sailsim.boat.Boat import Boat
from sailsim.wind.Wind import Wind

# Import Winds
from sailsim.wind.Windfield import Windfield
from sailsim.wind.Fluctuationfield import Fluctuationfield
from sailsim.wind.Squallfield import Squallfield

from sailsim.gui.ConfigWind import ConfigWind
from sailsim.gui.ConfigBoat import ConfigBoat
from sailsim.gui.SailsimGUI import SailsimGUI

OUTPUT_PATH = "..\\..\\MATLAB\\sailsim\\out.csv"

# Define Wind
wf = Windfield(0, 10)
flctf = Fluctuationfield(1)
sqf = Squallfield(0, 0, 100, 1, 0) # TODO has to be enabled later
wind = Wind([wf, flctf, sqf])
ConfigWind(wind).mainloop()
(windSpeed, windDir) = wind.getWind(0, 0, 0)

# Boat definition
b = Boat(0, 0)
b.setDirectionDeg(45)
b.setMainSailAngleDeg(45)
ConfigBoat(b, windDir).mainloop()

# Create world and simulation
w = World(b, wind, None)
s = Simulation(w, 0.01, 1024)

# Simulate 1 step
s.step()

# Finish simulation
s.run()
s.frameList.saveCSV(OUTPUT_PATH)

SailsimGUI(s).mainloop()
