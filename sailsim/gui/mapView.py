"""This module contains the class declaration for the MapViewWidget."""

from PySide6.QtCore import QPointF, Qt
from PySide6.QtGui import QCursor, QPainter, QPainterPath
from PySide6.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsView, QGraphicsScene

from sailsim.gui.qgraphicsitems import GUIBoat, GUIPath

# Map constants
ZOOMINFACTOR = 1.25
ZOOMOUTFACTOR = 1 / ZOOMINFACTOR
SCROLLSTEP = 10


def pointsToPath(points, jump=1):
    """Convert a pointlist into a QPainterPath."""
    path = QPainterPath()
    path.moveTo(QPointF(points[0][0], -points[0][1]))
    for i in range(0, len(points), jump)[1:]:
        point = points[i]
        path.lineTo(QPointF(point[0], -point[1]))
    return path


class MapViewScene(QGraphicsScene):
    """Map Widget that displays the boat and its path."""

    offset = QPointF()
    scale = 4
    lastDragPos = QPointF()

    waypointsLink = QPainterPath()
    waypoints = QPainterPath()
    path = QPainterPath()

    # Display proerties
    displayWaypointLink = True
    displayWaypoints = True
    displayPath = True

    def __init__(self, boat, parent=None):
        """
        Create a MapViewScene.

        Args:
            boat: Boat      Boat of the simulation
            parent          Parent of the QGraphicsScene
        """
        super().__init__(parent)

        self.boat = GUIBoat(boat)
        self.path = GUIPath(boat)
        self.addItem(self.boat)
        self.addItem(self.path)

        # Make area scrollable beyond boat boundaries
        # TODO find nicer way to do this
        self.addItem(QGraphicsRectItem(-2048, -2048, 4096, 4096))

    def viewFrame(self, framenumber):
        """Set the boat to a position saved in a frame given."""
        self.boat.setFrame(framenumber)


class MapViewView(QGraphicsView):
    """QT Viewport for viewing the MapViewScene."""

    def __init__(self, parent=None):
        """Create and configure MapViewView object."""
        super().__init__(parent)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setRenderHints(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def keyPressEvent(self, event):
        """Move mapView according to the button pressed."""
        # TODO translation is not working
        if event.key() == Qt.Key_Plus:
            self.zoom(ZOOMINFACTOR)
        elif event.key() == Qt.Key_Minus:
            self.zoom(ZOOMOUTFACTOR)
        elif event.key() == Qt.Key_Left:
            self.scroll(+SCROLLSTEP, 0)
        elif event.key() == Qt.Key_Right:
            self.scroll(-SCROLLSTEP, 0)
        elif event.key() == Qt.Key_Down:
            self.scroll(0, -SCROLLSTEP)
        elif event.key() == Qt.Key_Up:
            self.scroll(0, +SCROLLSTEP)
        else:
            super().keyPressEvent(event)

    def wheelEvent(self, event):
        """Zoom in and out when mouse wheel is moved."""
        numDegrees = event.angleDelta().y() / 8
        numSteps = numDegrees / 32
        self.zoom(pow(ZOOMINFACTOR, numSteps))

    def zoom(self, zoomFactor):
        """Zoom the mapView and keep mouse in the same spot."""
        self.scale(zoomFactor, zoomFactor)
        delta_x, delta_y = (QPointF(self.mapFromGlobal(QCursor.pos())) * (1 - zoomFactor)).toTuple()
        self.translate(delta_x, delta_y)


def main():
    """Run simple test program."""
    import sys

    from sailsim.boat.Boat import Boat

    app = QApplication(sys.argv)
    view = MapViewView()
    view.setScene(MapViewScene(Boat()))
    view.show()
    window = app.exec()
    sys.exit(window)


if __name__ == '__main__':
    main()
