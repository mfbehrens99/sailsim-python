from tkinter import *


class ControlBar(Frame):
    frame = 0
    def __init__(self, root):
        super().__init__(root)

        self.buttonStart = Button(self, text="|<", command=None)
        self.buttonStart.pack(side=LEFT)
        self.buttonPlay = Button(self, text=">", command=None)
        self.buttonPlay.pack(side=LEFT)
        self.buttonEnd = Button(self, text=">|", command=None)
        self.buttonEnd.pack(side=LEFT)

        self.labelFrameText = StringVar()
        self.labelFrameText.set(str(self.frame).zfill(4) + "/1023")
        self.labelFrame = Label(self, textvariable=self.labelFrameText)
        self.labelFrame.pack(side=LEFT)

        self.scaleTime = Scale(self, from_=0, to=1024, showvalue=False, orient=HORIZONTAL, command=self.updateFrame)
        self.scaleTime.set(0)
        self.scaleTime.pack(fill='x')

    def updateFrame(self, value):
        self.labelFrameText.set(str(value).zfill(4) + "/1023")
        self.frame = value
