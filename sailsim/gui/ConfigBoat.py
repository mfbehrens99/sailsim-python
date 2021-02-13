from tkinter import Tk, Frame, Label, Entry, Scale, StringVar, Canvas, Button
from tkinter import HORIZONTAL, RIGHT
from math import pi, sin, cos

from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval


class ConfigBoat(Tk):
    def __init__(self, boat):
        """Create a boat config window."""
        super().__init__()
        self.title("Configure Boat")

        self.boat = boat

        # Position and rotation control
        self.posControl = Frame(self)
        self.posControl.pack()

        self.varPosX = StringVar()
        self.varPosX.set(str(self.boat.posX))
        self.varPosY = StringVar()
        self.varPosY.set(str(self.boat.posY))
        Label(self.posControl, text="Position").grid(row=0, column=0)
        Entry(self.posControl, textvar=self.varPosX, width=5, justify="center").grid(row=0, column=1)
        Entry(self.posControl, textvar=self.varPosY, width=5, justify="center").grid(row=0, column=2)

        self.varSpeedX = StringVar()
        self.varSpeedX.set(str(self.boat.speedX))
        self.varSpeedX.trace("w", self.updateCanvasSpeedVector)
        self.varSpeedY = StringVar()
        self.varSpeedY.set(str(self.boat.speedY))
        self.varSpeedY.trace("w", self.updateCanvasSpeedVector)
        Label(self.posControl, text="Speed").grid(row=1, column=0)
        Entry(self.posControl, textvar=self.varSpeedX, width=5, justify="center").grid(row=1, column=1)
        Entry(self.posControl, textvar=self.varSpeedY, width=5, justify="center").grid(row=1, column=2)

        self.scaleDir = Scale(self.posControl, from_=-180, to=180, length=250, command=self.updateCanvasBoat, label="Boat Direction:", resolution=0.1, orient=HORIZONTAL, showvalue=True)
        self.scaleDir.set(round(self.boat.direction * 180 / pi, 1))
        self.scaleDir.grid(row=2, column=0, columnspan=3)

        self.scaleMainSail = Scale(self.posControl, from_=-90, to=90, length=250, command=self.updateCanvasMainSailAngle, label="Main Sail Angle:", resolution=0.1, orient=HORIZONTAL, showvalue=True)
        self.scaleMainSail.set(round(self.boat.mainSailAngle * 180 / pi, 1))
        self.scaleMainSail.grid(row=3, column=0, columnspan=3)


        # Display Canvas
        self.canvasDisp = Canvas(self, width=250, height=200)
        self.canvasDisp.pack()
        self.cpX, self.cpY = (125, 100)
        self.arrLen = 75

        self.canvasDisp.create_oval(self.cpX - self.arrLen * 1.25, self.cpY - self.arrLen * 1.25, self.cpX + self.arrLen * 1.25, self.cpY + self.arrLen * 1.25)
        # TODO draw compass
        self.boatArrow = self.canvasDisp.create_line(self.cpX, self.cpY + self.arrLen, self.cpX, self.cpY - self.arrLen, tags=("line"), arrow="last", width=4)
        self.mainSailArrow = self.canvasDisp.create_line(self.cpX, self.cpY, self.cpX, self.cpY + self.arrLen) # mainSailAngle
        self.speedVector = self.canvasDisp.create_line(self.cpX, self.cpY, self.cpX, self.cpY, tags=("line"), arrow="last", fill="orange") # speedVector


        # Static properties
        self.frameStatic = Frame(self)
        self.frameStatic.pack()
        self.varMass = StringVar()
        self.varMass.set(self.boat.mass)
        Label(self.frameStatic, text="Mass").grid(row=0, column=0)
        Entry(self.frameStatic, textvar=self.varMass, width=5, justify="right").grid(row=0, column=1)
        Label(self.frameStatic, text="kg").grid(row=0, column=2)

        self.varSailArea = StringVar()
        self.varSailArea.set(self.boat.sailArea)
        Label(self.frameStatic, text="Sail Area").grid(row=1, column=0)
        Entry(self.frameStatic, textvar=self.varSailArea, width=5, justify="right").grid(row=1, column=1)
        Label(self.frameStatic, text="m²").grid(row=1, column=2)

        self.varHullArea = StringVar()
        self.varHullArea.set(self.boat.hullArea)
        Label(self.frameStatic, text="Hull Area").grid(row=2, column=0)
        Entry(self.frameStatic, textvar=self.varHullArea, width=5, justify="right").grid(row=2, column=1)
        Label(self.frameStatic, text="m²").grid(row=2, column=2)

        self.varCenterboardArea = StringVar()
        self.varCenterboardArea.set(self.boat.centerboardArea)
        Label(self.frameStatic, text="Centerboard Area").grid(row=3, column=0)
        Entry(self.frameStatic, textvar=self.varCenterboardArea, width=5, justify="right").grid(row=3, column=1)
        Label(self.frameStatic, text="m²").grid(row=3, column=2)


        # Exit buttons
        self.buttonOk = Button(self, text="Ok", command=self.commandOk)
        self.buttonOk.pack(side=RIGHT)
        self.buttonExit = Button(self, text="Exit", command=self.commandExit)
        self.buttonExit.pack(side=RIGHT)
        self.buttonSave = Button(self, text="Save", command=self.commandSave)
        self.buttonSave.pack(side=RIGHT)

    # Exit button methods
    def commandOk(self):
        """Save and leave window."""
        self.commandSave()
        self.destroy()

    def commandExit(self):
        """Exit without saving."""
        self.destroy()

    def commandSave(self):
        """Save all settings in self.boat."""
        # TODO this method can be improved after Boat() got some more setter methods
        self.boat.posX = parseToFloat(self.varPosX.get())
        self.boat.posY = parseToFloat(self.varPosY.get())
        self.boat.speedX = parseToFloat(self.varSpeedX.get())
        self.boat.speedY = parseToFloat(self.varSpeedY.get())
        self.boat.direction = angleKeepInterval(self.scaleDir.get() * pi / 180)
        self.boat.mainSailAngle = directionKeepInterval(self.scaleMainSail.get() * pi / 180)

        self.boat.mass = parseToFloat(self.varMass.get())
        self.boat.sailArea = parseToFloat(self.varSailArea.get())
        self.boat.hullArea = parseToFloat(self.varHullArea.get())
        self.boat.centerboardArea = parseToFloat(self.varCenterboardArea.get())

    # Canvas update methods
    def updateCanvasBoat(self, *args):
        """Update direction of boat arrow based on scale position of direction. Also updates the main sail."""
        rad = float(self.scaleDir.get()) * pi / 180
        moveX, moveY = self.arrLen * sin(-rad), self.arrLen * cos(rad)
        self.canvasDisp.coords(self.boatArrow, self.cpX + moveX, self.cpY + moveY, self.cpX - moveX, self.cpY - moveY)
        self.updateCanvasMainSailAngle()

    def updateCanvasMainSailAngle(self, *args):
        """Update the main sail line."""
        rad = (self.scaleMainSail.get() - self.scaleDir.get()) * pi / 180
        moveX, moveY = self.arrLen * sin(rad), self.arrLen * cos(rad)
        self.canvasDisp.coords(self.mainSailArrow, self.cpX, self.cpY, self.cpX + moveX, self.cpY + moveY)

    def updateCanvasSpeedVector(self, *args):
        """Update initial boat speed vector based on entry fields."""
        entryX = parseToFloat(self.varSpeedX.get())
        entryY = parseToFloat(self.varSpeedY.get())
        self.canvasDisp.coords(self.speedVector, self.cpX, self.cpY, self.cpX + entryX * 10, self.cpY - entryY * 10)



def parseToFloat(val):
    """Convert a string to int or float. Return 0 if it is NaN."""
    if val.isnumeric():
        return int(val)
    try:
        return float(val)
    except ValueError:
        return 0
