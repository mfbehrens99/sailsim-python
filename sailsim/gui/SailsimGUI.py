"""This class is the main GUI for the sailsim project."""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from sailsim.gui.qtmain import Ui_MainWindow

from sailsim.gui.mapView import pointsToPath


class SailsimGUI(QMainWindow):
    """Main GUI for sailsim."""

    def __init__(self, simulation):
        super().__init__()

        self.simulation = simulation

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.timeSlider.setMaximum(len(simulation))

        self.updateFrame(0)
        self.updatePath(10)

    def updateFrame(self, frameNr):
        """Update display when the frame changed."""
        frames = self.simulation.frameList.frames
        if frameNr < len(frames):
            frame = frames[frameNr]

            # Update widgets
            maxFrame = str(len(self.simulation))
            self.ui.frameNr.setText(str(frameNr).zfill(len(maxFrame)) + "/" + maxFrame)
            self.ui.mapView.viewFrame(frame)
            # self.ui.boatInspector.viewFrame(frame)

    def updatePath(self, pathStep):
        """Update the path displayed on the MapViewWidget with the current data from the simulation."""
        path = pointsToPath(self.simulation.frameList.getCoordinateList(), pathStep)
        self.ui.mapView.setPath(path)


def main():
    app = QApplication(sys.argv)

    window = SailsimGUI()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
