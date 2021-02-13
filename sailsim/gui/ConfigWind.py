from tkinter import *

from sailsim.wind.Wind import Wind
from sailsim.wind.Windfield import Windfield
from sailsim.wind.Fluctuationfield import Fluctuationfield


class ConfigWind(Tk):
    def __init__(self, wind):
        super().__init__()
        self.title("Configure Boat")

        self.wind = wind

        self.list = Listbox(self, selectmode="browse")
        self.list.grid(row=0, column=0)
        self.insertWinds()

        self.info = Frame()
        self.info.grid(row=0, column=1)

        Entry(self.info, text="test").pack()



    def insertWinds(self):
        for wind in self.wind.winds:
            self.list.insert("end", str(type(wind))[21:-2])


if __name__ == "__main__":
    wf = Windfield(4, 2)
    f = Fluctuationfield()
    w = Wind([wf, f])
    cw = ConfigWind(w)
    cw.mainloop()
