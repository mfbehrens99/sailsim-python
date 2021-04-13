"""This class is the main GUI for the sailsim project."""

import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
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
        """Move to the next frame if it exists."""
        self.ui.timeSlider.setValue(self.ui.timeSlider.value() + 1)

    def decFrame(self):
        """Move to the previous """
        self.ui.timeSlider.setValue(self.ui.timeSlider.value() - 1)

    def pressedPlay(self, active):
        """"""
        if active:
            if self.simulation.lastFrame > self.frame:
                self.timer.start()
            else:
                self.playStop()
        else:
            self.playStop()

    def playStop(self):
        self.timer.stop()
        self.ui.buttonPlay.setChecked(False)

    def playStep(self):
        if self.simulation.lastFrame > self.frame:
            self.incFrame()
        else:
            self.playStop()


def main():
    app = QApplication(sys.argv)

    window = SailsimGUI()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
