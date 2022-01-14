"""This class is the main GUI for the sailsim project."""

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow

from sailsim.gui.boatInspector import BoatInspectorScene
from sailsim.gui.mapView import MapViewScene
from sailsim.gui.qtmain import Ui_MainWindow


class SailsimGUI(QMainWindow):
    """Main GUI for sailsim."""

    def __init__(self, simulation):
        """
        Create SailsimGUI object.

        Args:
            simulation      Simulation that should be displayed
        """
        super().__init__()

        self.simulation = simulation
        self.frame = 0

        # Load UI from QT generated file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Playback and timeSlider
        self.timer = QTimer(self)
        self.timer.setInterval(simulation.timestep * 1000)
        self.timer.timeout.connect(self.playStep)
        self.ui.timeSlider.setMaximum(len(simulation))
        self.ui.timeSlider.setValue(self.frame)

        # set up map view
        self.mapViewScene = MapViewScene(simulation.boat)
        self.ui.mapView.setScene(self.mapViewScene)

        # set up boat inspector
        self.boatInspectorScene = BoatInspectorScene(simulation.boat)
        self.ui.boatInspector.setScene(self.boatInspectorScene)

        # if self.simulation.boat.sailor is not None:
        #     self.ui.mapView.setWaypoints(self.simulation.boat.sailor.commandList)
        self.updateFrame(0)
        # self.updateViewStates()

    def updateFrame(self, framenumber):
        """Update display when the frame changed."""
        frames = self.simulation.boat.frameList.frames
        if framenumber < len(frames):
            self.frame = framenumber
            frame = frames[framenumber]

            # Update widgets
            maxFrame = str(len(self.simulation))
            self.ui.frameNr.setText(str(framenumber).zfill(len(maxFrame)) + "/" + maxFrame)
            self.mapViewScene.viewFrame(framenumber)
            self.boatInspectorScene.viewFrame(framenumber)
            self.ui.valueInspector.viewFrame(frame)

    def incFrame(self):
        """Move to the next frame if it is in the range of the slider."""
        self.ui.timeSlider.setValue(self.ui.timeSlider.value() + 1)

    def decFrame(self):
        """Move to the previous frame if it is in the range of the slider."""
        self.ui.timeSlider.setValue(self.ui.timeSlider.value() - 1)

    def startFrame(self):
        """Move slider to the frist Frame."""
        self.ui.timeSlider.setValue(self.ui.timeSlider.minimum())

    def endFrame(self):
        """Move slider to the last Frame."""
        self.ui.timeSlider.setValue(self.ui.timeSlider.maximum())

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

    def updateViewStates(self):
        """Load states for QActions from child widgets."""
        # Import states from mapView
        self.ui.actionShowWaypointLink.setChecked(self.ui.mapView.displayWaypointLink)
        self.ui.actionShowWaypoints.setChecked(self.ui.mapView.displayWaypoints)
        self.ui.actionShowMainSailMapView.setChecked(self.ui.mapView.boat.displayMainSail)
        self.ui.actionShowRudderMapView.setChecked(self.ui.mapView.boat.displayRudder)

        # Import states from boatInspector
        self.ui.actionShowBoat.setChecked(self.ui.boatInspector.displayBoat)
        self.ui.actionShowRudderBoatInspector.setChecked(self.ui.boatInspector.displayRudder)
        self.ui.actionShowMainSailBoatInspector.setChecked(self.ui.boatInspector.displayMainSail)
        self.ui.actionShowBoatDirection.setChecked(self.ui.boatInspector.displayBoatDirection)
        self.ui.actionShowSpeed.setChecked(self.ui.boatInspector.displaySpeed)
        self.ui.actionShowForces.setChecked(self.ui.boatInspector.displayForces)

        # Disable actions if boat is hidden
        self.ui.actionShowRudderBoatInspector.setEnabled(self.ui.boatInspector.displayBoat)
        self.ui.actionShowMainSailBoatInspector.setEnabled(self.ui.boatInspector.displayBoat)

    from .actionslots import actionViewShowWaypointLink, actionViewShowWaypoints, actionViewShowMainSailMapView, actionViewShowRudderMapView
    from .actionslots import actionViewShowBoat, actionViewShowBoatDirection, actionViewShowSpeed, actionViewShowMainSailBoatInspector, actionViewShowRudderBoatInspector, actionViewShowForces
