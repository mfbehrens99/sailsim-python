from tkinter import Tk

from sailsim.gui.SailsimMenu import SailsimMenu
from sailsim.gui.Map import Map
from sailsim.gui.ControlBar import ControlBar

main = Tk()
main.title("Sailsim GUI")
main.state('zoomed')

menu = SailsimMenu()
main.config(menu=menu)

mainMap = Map(main)
mainMap.pack(fill="both", expand=True)

controlBar = ControlBar(main)
controlBar.pack(side="bottom", fill="x")

main.mainloop()
