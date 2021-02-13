from tkinter import Menu


class SailsimMenu(Menu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        menuFile = Menu()
        self.add_cascade(label="File", menu=menuFile)
        menuFile.add_command(label="New", command=None)
        menuFile.add_command(label="Open", command=None)
        menuFile.add_command(label="Save", command=None)

        menuEdit = Menu()
        self.add_cascade(label="Edit", menu=menuEdit)
        menuEdit.add_command(label="Run", command=None)
        menuEdit.add_command(label="Step", command=None)
        menuEdit.add_command(label="Run Range", command=None)
        menuEdit.add_command(label="Run Live", command=None)

        menuView = Menu()
        self.add_cascade(label="View", menu=menuView)
        menuView.add_command(label="Show/Hide ControlBar", command=None)

        menuHelp = Menu()
        self.add_cascade(label="Help", menu=menuHelp)
        menuHelp.add_command(label="Open Project on GitHub", command=None)
