from tkinter import Tk, Frame, Label, Entry, Button, Listbox, StringVar, Canvas, messagebox
from math import pi

from sailsim.utils.conversion import stringToFloat
from sailsim.utils.coordconversion import cartToPolar, polarToCart

from sailsim.wind.Wind import Wind
from sailsim.wind.Windfield import Windfield
from sailsim.wind.Fluctuationfield import Fluctuationfield
from sailsim.wind.Squallfield import Squallfield

from sailsim.gui.tkinterutils import exitMsg, drawCompass


class ConfigWind(Tk):
    def __init__(self, wind):
        super().__init__()
        self.title("Configure Boat")

        self.wind = wind

        self.list = Listbox(self, selectmode="browse", exportselection=False)
        self.list.grid(row=0, column=0, columnspan=2, sticky="ns")
        self.list.bind("<<ListboxSelect>>", self.windChanged)

        self.info = Frame()
        self.info.grid(row=0, column=2, columnspan=3)
        self.windFrames = []

        self.insertWinds()

        self.selection = 0
        self.list.select_set(0)
        self.showWind(0)

        Button(self, text="Add").grid(row=1, column=0, sticky="w")
        Button(self, text="Remove", command=self.remove).grid(row=1, column=1, sticky="w")
        # TODO implement these functions

        Button(self, text="Cancel", command=self.buttonCancel).grid(row=1, column=2, sticky="e")
        Button(self, text="Apply", command=self.buttonApply).grid(row=1, column=3, sticky="e")
        Button(self, text="Ok", command=self.buttonOk).grid(row=1, column=4, sticky="e")



    def insertWinds(self):
        self.list.delete(0)
        self.windFrames = []
        for i in range(len(self.wind.winds)):
            wind = self.wind.winds[i]
            self.list.insert("end", str(i + 1) + ": " + wind.name)
            windFrame = WINDFIELD_TO_FRAME[type(wind)](self.info, wind)
            self.windFrames.append(windFrame)
            windFrame.grid(row=0, column=0, sticky="nsew")
            windFrame.read()


    def windChanged(self, event):
        self.selection = event.widget.curselection()[0]
        self.showWind(self.selection)

    def showWind(self, nr):
        windFrame = self.windFrames[nr]
        windFrame.tkraise()

    def buttonApply(self):
        for windFrame in self.windFrames:
            windFrame.write()

    def buttonCancel(self):
        exitMsg(self.buttonApply, self)

    def buttonOk(self):
        self.buttonApply()
        self.destroy()

    def remove(self):
        if messagebox.askyesno("Delete", "Are You Sure?", icon='question', default='no'):
            del self.wind.winds[self.selection]
            if len(self.wind) > 0:
                self.list.delete(self.selection)
                self.selection = max(0, self.selection - 1)
                self.showWind(self.selection)
            else:
                self.destoy()


class FrameWindfield(Frame):
    def __init__(self, root, wind):
        super().__init__(root)
        self.wind = wind

        self.varName = StringVar()
        self.varSpeed = StringVar()
        self.varSpeed.trace("w", self.updateWindVector)
        self.varDir = StringVar()
        self.varDir.trace("w", self.updateWindVector)
        Label(self, text="Name").grid(row=0, column=0, sticky="W")
        Entry(self, textvar=self.varName).grid(row=0, column=1)

        self.cp = 75
        self.windCanvas = Canvas(self, width=150, height=150)
        drawCompass(self.windCanvas, self.cp, self.cp, 10, 50, 73, "grey", "white")
        self.windCanvas.grid(row=1, column=0, columnspan=2, sticky="W")
        self.windArrow = self.windCanvas.create_line(self.cp, self.cp, self.cp, self.cp, tags=("line"), arrow="last", fill="blue")

        Label(self, text="Wind speed").grid(row=2, column=0, sticky="W")
        Entry(self, textvar=self.varSpeed).grid(row=2, column=1)
        Label(self, text="m/s").grid(row=2, column=2, sticky="W")
        Label(self, text="Wind dir").grid(row=3, column=0, sticky="W")
        Entry(self, textvar=self.varDir).grid(row=3, column=1)
        Label(self, text="°").grid(row=3, column=2, sticky="W")

        self.updateWindVector()

    def read(self):
        w = self.wind
        self.varName.set(w.name)
        (speed, direction) = cartToPolar(w.speedX, w.speedY)
        self.varSpeed.set(speed)
        self.varDir.set(direction * 180 / pi)

    def write(self):
        w = self.wind
        w.name = self.varName.get()
        speed = stringToFloat(self.varSpeed.get())
        direction = stringToFloat(self.varDir.get()) * pi / 180
        (w.speedX, w.speedY) = polarToCart(speed, direction)

    def updateWindVector(self, *args):
        if stringToFloat(self.varSpeed.get()) == 0:
            self.windCanvas.coords(self.windArrow, 0, 0, -10, -10)
        else:
            direction = stringToFloat(self.varDir.get()) * pi / 180
            (vecX, vecY) = polarToCart(70, direction)
            self.windCanvas.coords(self.windArrow, self.cp, self.cp, self.cp + vecX, self.cp - vecY)


class FrameFluctuationfield(FrameWindfield):
    def __init__(self, root, wind):
        super().__init__(root, wind)

        self.varAmplitude = StringVar()
        self.varScale = StringVar()
        self.varRate = StringVar()
        Label(self, text="Amplitude").grid(row=4, column=0, sticky="W")
        Entry(self, textvar=self.varAmplitude).grid(row=4, column=1)
        Label(self, text="m/s").grid(row=4, column=2, sticky="W")
        Label(self, text="Scale").grid(row=5, column=0, sticky="W")
        Entry(self, textvar=self.varScale).grid(row=5, column=1)
        Label(self, text="m").grid(row=5, column=2, sticky="W")
        Label(self, text="Speed").grid(row=6, column=0, sticky="W")
        Entry(self, textvar=self.varRate).grid(row=6, column=1)

    def read(self):
        super().read()
        self.varAmplitude.set(self.wind.amplitude)
        self.varScale.set(self.wind.getScale())
        self.varRate.set(self.wind.getSpeed())

    def write(self):
        super().write()
        w = self.wind
        w.amplitude = stringToFloat(self.varAmplitude.get())
        w.setScale(stringToFloat(self.varScale.get()))
        w.setSpeed(stringToFloat(self.varRate.get()))


class FrameSquallfield(FrameWindfield):
    def __init__(self, root, wind):
        super().__init__(root, wind)

        self.varGridDistance = StringVar()
        self.varDisplacementFactor = StringVar()
        Label(self, text="Grid distance").grid(row=4, column=0, sticky="W")
        Entry(self, textvar=self.varGridDistance).grid(row=4, column=1)
        Label(self, text="m").grid(row=4, column=2, sticky="W")
        Label(self, text="Displ factor").grid(row=5, column=0, sticky="W")
        Entry(self, textvar=self.varDisplacementFactor).grid(row=5, column=1)

    def read(self):
        super().read()
        self.varGridDistance.set(self.wind.gridDistance)
        self.varDisplacementFactor.set(self.wind.displacementFactor)

    def write(self):
        super().write()
        w = self.wind
        w.varGridDistance = stringToFloat(self.varGridDistance.get())
        w.displacementFactor = stringToFloat(self.varDisplacementFactor.get())


WINDFIELD_TO_FRAME = {Windfield: FrameWindfield, Fluctuationfield: FrameFluctuationfield, Squallfield: FrameSquallfield}


if __name__ == "__main__":
    wf = Windfield(4, 2)
    f = Fluctuationfield()
    s = Squallfield(4, 2, 10)
    w = Wind([wf, f, s])
    cw = ConfigWind(w)
    cw.mainloop()
