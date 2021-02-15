from tkinter import Tk, Frame, Entry, Button, Listbox, StringVar

from sailsim.utils.conversion import stringToFloat

from sailsim.wind.Wind import Wind
from sailsim.wind.Windfield import Windfield
from sailsim.wind.Fluctuationfield import Fluctuationfield
from sailsim.wind.Squallfield import Squallfield

from sailsim.gui.dialogs import exitMsg


class ConfigWind(Tk):
    def __init__(self, wind):
        super().__init__()
        self.title("Configure Boat")

        self.wind = wind

        self.list = Listbox(self, selectmode="browse", exportselection=False)
        self.list.grid(row=0, column=0, columnspan=2)
        self.list.bind("<<ListboxSelect>>", self.windChanged)

        self.info = Frame()
        self.info.grid(row=0, column=2, columnspan=3)
        self.windFrames = []

        self.insertWinds()

        self.list.select_set(0)
        self.showWind(0)

        Button(self, text="Add").grid(row=1, column=0)
        Button(self, text="Remove").grid(row=1, column=1)

        Button(self, text="Save", command=self.buttonSave).grid(row=1, column=2)
        Button(self, text="Exit", command=self.buttonExit).grid(row=1, column=3)
        Button(self, text="Ok", command=self.buttonOk).grid(row=1, column=4)



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
        selection = event.widget.curselection()[0]
        self.showWind(selection)

    def showWind(self, nr):
        windFrame = self.windFrames[nr]
        windFrame.tkraise()

    def buttonSave(self):
        for windFrame in self.windFrames:
            windFrame.write()

    def buttonExit(self):
        exitMsg(self.buttonSave, self)

    def buttonOk(self):
        self.buttonSave()
        self.destroy()


class FrameWindfield(Frame):
    def __init__(self, root, wind):
        super().__init__(root)
        self.wind = wind

        self.varName = StringVar()
        self.varX = StringVar()
        self.varY = StringVar()
        Entry(self, textvar=self.varName).pack()
        Entry(self, textvar=self.varX).pack()
        Entry(self, textvar=self.varY).pack()

    def read(self):
        w = self.wind
        self.varName.set(w.name)
        self.varX.set(w.speedX)
        self.varY.set(w.speedY)

    def write(self):
        w = self.wind
        w.name = self.varName.get()
        w.speedX = stringToFloat(self.varX.get())
        w.speedY = stringToFloat(self.varY.get())


class FrameFluctuationfield(FrameWindfield):
    def __init__(self, root, wind):
        super().__init__(root, wind)

        self.varAmplitude = StringVar()
        self.varScale = StringVar()
        self.varSpeed = StringVar()
        Entry(self, textvar=self.varAmplitude).pack()
        Entry(self, textvar=self.varScale).pack()
        Entry(self, textvar=self.varSpeed).pack()

    def read(self):
        super().read()
        self.varAmplitude.set(self.wind.amplitude)
        self.varScale.set(self.wind.getScale())
        self.varSpeed.set(self.wind.getSpeed())

    def write(self):
        super().write()
        w = self.wind
        w.amplitude = stringToFloat(self.varAmplitude.get())
        w.setScale(stringToFloat(self.varScale.get()))
        w.setSpeed(stringToFloat(self.varSpeed.get()))


class FrameSquallfield(FrameWindfield):
    def __init__(self, root, wind):
        super().__init__(root, wind)

        self.varGridDistance = StringVar()
        self.varDisplacementFactor = StringVar()
        Entry(self, textvar=self.varGridDistance).pack()
        Entry(self, textvar=self.varDisplacementFactor).pack()

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
