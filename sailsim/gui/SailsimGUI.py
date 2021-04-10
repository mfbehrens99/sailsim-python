"""This class is the main GUI for the sailsim project."""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from sailsim.gui.qtmain import Ui_MainWindow


class SailsimGUI(QMainWindow):
    """Main GUI for sailsim."""

    def __init__(self, simulation):
        super().__init__()

        self.simulation = simulation

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def updateFrame(self, frameNr):
        """Update display when the frame changed."""
        frames = self.simulation.frameList.frames
        if frameNr < len(frames):
            frame = frames[frameNr]

            # Update widgets
            self.ui.frameNr.setText(str(frameNr).zfill(4) + "/1000")
            self.ui.mapView.viewFrame(frame)
            # self.ui.boatInspector.viewFrame(frame)


def main():
    app = QApplication(sys.argv)

    window = SailsimGUI()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
