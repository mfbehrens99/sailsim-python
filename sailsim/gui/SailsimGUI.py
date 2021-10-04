"""This class is the main GUI for the sailsim project."""

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow
from sailsim.gui.qtmain import Ui_MainWindow

from sailsim.gui.mapView import pointsToPath


class SailsimGUI(QMainWindow):
    """Main GUI for sailsim."""

    def __init__(self, simulation):
        super().__init__()

        self.simulation = simulation
        self.frame = 0

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer(self)
        self.timer.setInterval(simulation.timestep * 1000)
        self.timer.timeout.connect(self.playStep)

        self.ui.timeSlider.setMaximum(len(simulation))
        self.ui.timeSlider.setValue(self.frame)
        if not self.simulation.world.boat.sailor is None:
            self.ui.mapView.setWaypoints(self.simulation.world.boat.sailor.commandList)
        self.updatePath(5)

    def updateFrame(self, frameNr):
        """Update display when the frame changed."""
        frames = self.simulation.frameList.frames
        if frameNr < len(frames):
            self.frame = frameNr
            frame = frames[frameNr]

            # Update widgets
            maxFrame = str(len(self.simulation))
            self.ui.frameNr.setText(str(frameNr).zfill(len(maxFrame)) + "/" + maxFrame)
            self.ui.mapView.viewFrame(frame)
            self.ui.boatInspector.viewFrame(frame)

    def updatePath(self, pathStep):
        """Update the path displayed on the MapViewWidget with the current data from the simulation."""
        path = pointsToPath(self.simulation.frameList.getCoordinateList(), pathStep)
        self.ui.mapView.setPath(path)

    def incFrame(self):
        """Move to the next frame if it is in the range of the slider."""
        self.ui.timeSlider.setValue(self.ui.timeSlider.value() + 1)

    def decFrame(self):
        """Move to the previous frame if it is in the range of the slider."""
        self.ui.timeSlider.setValue(self.ui.timeSlider.value() - 1)

    def pressedPlay(self, active):
        """Start or stop animation depending on active."""
        if active:
            if self.simulation.lastFrame > self.frame:
                self.timer.start()
            else:
                self.playStop()
        else:
            self.playStop()

    def playStop(self):
        """Stop the animation and uncheck the play button."""
        self.timer.stop()
        self.ui.buttonPlay.setChecked(False)

    def playStep(self):
        """Increase the frame if it is still available. Otherwise stop the animation."""
        if self.simulation.lastFrame > self.frame:
            self.incFrame()
        else:
            self.playStop()
