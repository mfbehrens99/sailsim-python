"""This module contains the class declaration of BoatInspectorWidget."""

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QMouseEvent, QPainter, QResizeEvent, QWheelEvent
from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsRectItem, QGraphicsView

from sailsim.boat.Boat import Boat
from sailsim.gui.qgraphicsitems import GUIBoatVectors, GUIBoat


class BoatInspectorScene(QGraphicsScene):
    """Display the state of the boat with all its properties."""

    displayBoat = True
    displayMainSail = True
    displayRudder = True
    displayBoatDirection = True
    displaySpeed = True
    displayForces = True

    def __init__(self, boat: Boat, parent=None) -> None:
        """
        Create a BoatInspectorScene object.

        Args:
            boat: Boat      Boat of the simulation
            parent          Parent of the QGraphicsScene
        """
        super().__init__(parent)

        self.setBackgroundBrush(QColor(156, 211, 219))

        background = QGraphicsRectItem(-8, -8, 16, 16)
        background.setPen(Qt.NoPen)
        self.addItem(background)

        self.boat = GUIBoat(boat)
        self.boat.allowMovement = False
        self.addItem(self.boat)

        self.boatVectors = GUIBoatVectors(boat)
        self.boatVectors.followBoat = False
        self.addItem(self.boatVectors)

    def viewFrame(self, framenumber):
        """Set the boat to a position saved in a frame given."""
        self.boat.setFrame(framenumber)
        self.boatVectors.setFrame(framenumber)
        self.update()


class BoatInspectorView(QGraphicsView):
    """QT Viewport for viewing the BoatInspectorScene."""

    def __init__(self, parent=None) -> None:
        """Create and configure MapViewView object."""
        super().__init__(parent)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setRenderHints(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        self.centerOn(0, 0)
        self.scale(32, 32)

    def resizeEvent(self, _event: QResizeEvent):
        """Keep size of the boatInspector at maximum size."""
        self.centerOn(0, 0)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """Snap boat inspector back to 0|0 when mouse is released."""
        super().mouseReleaseEvent(event)
        if event.button() == Qt.LeftButton:
            self.centerOn(0, 0)

    def wheelEvent(self, _event: QWheelEvent) -> None:
        """Disable scrolling."""


def main():
    """Run simple test program."""
    import sys
    app = QApplication(sys.argv)
    view = BoatInspectorView()
    view.setScene(BoatInspectorScene(Boat()))
    view.show()
    window = app.exec()
    sys.exit(window)


if __name__ == '__main__':
    main()