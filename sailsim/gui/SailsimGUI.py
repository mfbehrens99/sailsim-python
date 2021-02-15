from tkinter import Tk

from sailsim.simulation.Simulation import Simulation
from sailsim.boat.Boat import Boat
from sailsim.wind.Wind import Wind
from sailsim.world.World import World
from sailsim.wind.Windfield import Windfield

from sailsim.gui.SailsimMenu import SailsimMenu
from sailsim.gui.Map import Map
from sailsim.gui.ControlBar import ControlBar


class SailsimGUI(Tk):
    def __init__(self, simulation):
        super().__init__()
        self.title("Sailsim GUI")
        self.state('zoomed')

        self.simulation = simulation
        self.simulation.run()

        self.menu = SailsimMenu()
        self.config(menu=self.menu)

        self.mainMap = Map(self, self.simulation.frameList)
        self.mainMap.pack(fill="both", expand=True)

        self.controlBar = ControlBar(self)
        self.controlBar.pack(side="bottom", fill="x")


    def updateBoat(self):
        (posX, posY, direction) = self.simulation.frameList.getBoat(int(self.controlBar.frame))
        self.mainMap.updateBoat(posX * 10, posY * 10, direction)


if __name__ == "__main__":
    b = Boat(10, 0, 80, 7, None)
    w = Wind([Windfield(10, 10)])
    s = Simulation(World(b, w, None), 0.001, 1024)
    sg = SailsimGUI(s)
    sg.mainloop()
