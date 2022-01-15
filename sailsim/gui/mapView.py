"""This module contains the class declaration for the MapViewWidget."""

from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QColor, QCursor, QKeyEvent, QPainter, QPen, QResizeEvent, QWheelEvent
from PySide6.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsScene, QGraphicsView

from sailsim.boat.Boat import Boat
from sailsim.gui.qgraphicsitems import GUIBoatVectors, GUIBoat, GUIBoatPath, GUIWaypoints

# map movements constants
ZOOM_IN_FACTOR = 1.25
ZOOM_OUT_FACTOR = 1 / ZOOM_IN_FACTOR
SCROLL_STEP = 10


class MapViewScene(QGraphicsScene):
    """Map Widget that displays the boat and its path."""

    def __init__(self, boat: Boat, parent=None) -> None:
        """
        Create a MapViewScene object.

        Args:
            boat: Boat      Boat of the simulation
            parent          Parent of the QGraphicsScene
        """
        super().__init__(parent)

        self.setBackgroundBrush(QColor(156, 211, 219))

        self.boat = GUIBoat(boat)
        self.addItem(self.boat)

        self.path = GUIBoatPath(boat)
        self.path.setPen(QPen(Qt.black, 2))
        self.addItem(self.path)

        self.boatVectors = GUIBoatVectors(boat)
        self.addItem(self.boatVectors)

        self.waypoints = GUIWaypoints(boat)
        self.addItem(self.waypoints)

        # Make area scrollable beyond boat boundaries
        # TODO find nicer way to do this
        self.addItem(QGraphicsRectItem(-2048, -2048, 4096, 4096))

    def viewFrame(self, framenumber: int) -> None:
        """Set the boat to a position saved in a frame given."""
        self.boat.setFrame(framenumber)
        self.boatVectors.setFrame(framenumber)
        self.update()


class MapViewView(QGraphicsView):
    """QT Viewport for viewing the MapViewScene."""

    def __init__(self, parent=None) -> None:
        """Create and configure MapViewView object."""
        super().__init__(parent)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setRenderHints(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        """Move mapView according to the button pressed."""
        # TODO translation is not working
        if event.key() == Qt.Key_Plus:
            self.zoom(ZOOM_IN_FACTOR)
        elif event.key() == Qt.Key_Minus:
            self.zoom(ZOOM_OUT_FACTOR)
        elif event.key() == Qt.Key_Left:
            self.scroll(SCROLL_STEP, 0)
        elif event.key() == Qt.Key_Right:
            self.scroll(-SCROLL_STEP, 0)
        elif event.key() == Qt.Key_Down:
            self.scroll(0, -SCROLL_STEP)
        elif event.key() == Qt.Key_Up:
            self.scroll(0, SCROLL_STEP)
        else:
            super().keyPressEvent(event)

    def resizeEvent(self, event: QResizeEvent):
        """Keep center point in center."""
        self.translate(event.size().width(), event.size().height())

    def wheelEvent(self, event: QWheelEvent) -> None:
        """Zoom in and out when mouse wheel is moved."""
        numDegrees = event.angleDelta().y() / 8
        numSteps = numDegrees / 32
        self.zoom(pow(ZOOM_IN_FACTOR, numSteps))

    def zoom(self, zoomFactor: float) -> None:
        """Zoom the mapView and keep mouse in the same spot."""
        self.scale(zoomFactor, zoomFactor)
        delta = (QPointF(self.mapFromGlobal(QCursor.pos())) * (1 - zoomFactor))
        self.translate(delta.x(), delta.y())


def main():
    """Run simple test program."""
    import sys
    app = QApplication(sys.argv)
    view = MapViewView()
    view.setScene(MapViewScene(Boat()))
    view.show()
    window = app.exec()
    sys.exit(window)


if __name__ == '__main__':
    main()
