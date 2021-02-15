from tkinter import *
# import random
from math import pi, sin, cos


class Map(Frame):
    def __init__(self, root, frameList):
        super().__init__(root)

        self.framelist = frameList

        self.canvas = Canvas(self, width=400, height=400)
        self.xsb = Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(-1000, -1000, 1000, 1000))

        # self.xsb.grid(row=1, column=0, sticky="ew")
        # self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # TODO removed this part
        # for n in range(50):
        #     x0 = random.randint(0, 900)
        #     y0 = random.randint(50, 900)
        #     x1 = x0 + random.randint(50, 100)
        #     y1 = y0 + random.randint(50, 100)
        #     color = ("red", "orange", "yellow", "green", "blue")[random.randint(0, 4)]
        #     self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill=color, activefill="black", tags=n)
        # self.canvas.create_text(50, 10, anchor="nw", text="Click and drag to move the canvas\nScroll to zoom.")

        self.canvasBoat = self.canvas.create_line(0, 0, 0, 0, width=10)

        coords = self.framelist.getCoordinateList()
        self.boatPath = self.canvas.create_line(coords)

        # This is what enables using the mouse:
        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_move)
        # linux scroll
        self.canvas.bind("<Button-4>", self.zoomerP)
        self.canvas.bind("<Button-5>", self.zoomerM)
        # windows scroll
        self.canvas.bind("<MouseWheel>", self.zoomer)

    # update Canvas
    def updateBoat(self, posX, posY, direction):
        boatLength = 4.2 * 10
        posY *= -1
        coords = [posX - sin(direction) * boatLength * 0.5, posY + cos(direction) * boatLength * 0.5, posX + sin(direction) * boatLength * 0.5, posY - cos(direction) * boatLength * 0.5]
        self.canvas.coords(self.canvasBoat, coords)

    # move
    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)
    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    # windows zoom
    def zoomer(self, event):
        if event.delta > 0:
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif event.delta < 0:
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # linux zoom
    def zoomerP(self, event):
        self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def zoomerM(self, event):
        self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def create_rectangle(self, *args, **kwargs):
        self.canvas.create_rectangle(*args, **kwargs)
