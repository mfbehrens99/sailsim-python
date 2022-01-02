"""This module contains the class declaration for the MapViewWidget."""

from math import pi, sin, cos

from PySide6.QtCore import QPoint, QPointF, Qt
from PySide6.QtGui import QCursor, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import QApplication, QWidget

from sailsim.sailor.Commands import Waypoint

# Map constants
ZoomInFactor = 1.25
ZoomOutFactor = 1 / ZoomInFactor
ScrollStep = 10


def pointsToPath(points, jump=1):
    """Convert a pointlist into a QPainterPath."""
    path = QPainterPath()
    path.moveTo(QPointF(points[0][0], -points[0][1]))
    for i in range(0, len(points), jump)[1:]:
        point = points[i]
        path.lineTo(QPointF(point[0], -point[1]))
    return path

class GUIBoat():
    position = QPointF(0, 0)
    direction = 0
    mainSailAngle = 0
    rudderAngle = 0

    path = None

    displayMainSail = True
    displayRudder = True
    displayPath = True

    def __init__(self, frameList):
        self.frameList = frameList
        self.updateBoatPath()

    def paintBoat(self, painter, scale):
        if self.displayPath:
            painter.setPen(QPen(Qt.darkGray, 4 / scale, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawPath(self.path)

        painter.translate(self.position)
        painter.rotate(self.direction)

        GUIBoat.drawBoatShape(painter, Qt.black)
        if self.displayMainSail:
            painter.setPen(QPen(Qt.green, 0.1, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(QPointF(0, 0), QPointF(-sin(self.mainSailAngle), cos(self.mainSailAngle)) * 2)
        if self.displayRudder:
            painter.setPen(QPen(Qt.blue, 0.1, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(QPointF(0, 2.2), QPointF(sin(self.rudderAngle), cos(self.rudderAngle)) * 0.5 + QPointF(0, 2.2))

    def set(self, frame):
        self.position = QPointF(frame.boatPosX, -frame.boatPosY)
        self.direction = frame.boatDirection / pi * 180
        self.mainSailAngle = frame.boatMainSailAngle
        self.rudderAngle = frame.boatRudderAngle

    def updateBoatPath(self, jump=1):
        """Convert a pointlist into a QPainterPath."""
        points = self.frameList.getCoordinateList()
        self.path = pointsToPath(points, jump)

    @staticmethod
    def drawBoatShape(painter, color):
        """Return the QPainterPath for drawing a boat."""
        painter.setPen(Qt.NoPen)
        painter.setBrush(color)
        boat = QPainterPath()
        boat.moveTo(0, -2)
        boat.cubicTo(QPointF(1, -.5), QPointF(1, .5), QPointF(.8, 2.2))
        boat.lineTo(-.8, 2.2)
        boat.cubicTo(QPointF(-1, .5), QPointF(-1, -.5), QPointF(0, -2))
        painter.drawPath(boat)


class MapViewWidget(QWidget):
    """Map Widget that displays the boat and its path."""

    windowWidth = 0
    windowHeight = 0

    offset = QPointF()
    scale = 4
    lastDragPos = QPointF()

    waypointsLink = QPainterPath()
    waypoints = QPainterPath()
    path = QPainterPath()

    boat = None

    # Display proerties
    displayWaypointLink = True
    displayWaypoints = True
    displayPath = True

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("MapViewWidget")
        self.setCursor(Qt.CrossCursor)
        self.resize(550, 400)

    def paintEvent(self, _event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        painter.translate(self.offset)
        painter.scale(self.scale, self.scale)

        if self.displayWaypointLink:
            painter.setPen(QPen(Qt.gray, .1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawPath(self.waypointsLink)
        if self.displayWaypoints:
            painter.setPen(QPen(Qt.blue, .1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawPath(self.waypoints)

        if self.displayPath:
            painter.setPen(QPen(Qt.darkGray, 4 / self.scale, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawPath(self.path)

        self.boat.paintBoat(painter, self.scale)

    def setBoat(self, boat):
        """Register a boat for the mapView."""
        self.boat = GUIBoat(boat.frameList)

    def setWaypoints(self, commands):
        """Display the waypoints in a commandList on mapView."""
        if len(commands) > 0:
            wpPath = QPainterPath()
            # TODO find out boat starting coordinates
            wpLinkList = [[0, 0]]
            for command in commands:
                if isinstance(command, Waypoint):
                    wpPath.addEllipse(QPoint(command.destX, -command.destY), command.radius, command.radius)
                    wpLinkList.append([command.destX, command.destY])
            self.waypointsLink = pointsToPath(wpLinkList)
            self.waypoints = wpPath
            self.update()

    def viewFrame(self, frame):
        """Set the boat to a position saved in a frame given."""
        self.boat.set(frame)
        self.update()

    def resizeEvent(self, event):
        """Keep center of the map in the center."""
        width, height = event.size().width(), event.size().height()
        self.offset -= QPoint((self.windowWidth - width) / 2, (self.windowHeight - height) / 2)
        self.windowWidth, self.windowHeight = width, height

    def keyPressEvent(self, event):
        """Move mapView according to the button pressed."""
        # TODO is this working?
        if event.key() == Qt.Key_Plus:
            self.zoomCenter(ZoomInFactor)
        elif event.key() == Qt.Key_Minus:
            self.zoomCenter(ZoomOutFactor)
        elif event.key() == Qt.Key_Left:
            self.scroll(+ScrollStep, 0)
        elif event.key() == Qt.Key_Right:
            self.scroll(-ScrollStep, 0)
        elif event.key() == Qt.Key_Down:
            self.scroll(0, -ScrollStep)
        elif event.key() == Qt.Key_Up:
            self.scroll(0, +ScrollStep)
        else:
            super().keyPressEvent(event)

    def wheelEvent(self, event):
        """Zoom in and out when mouse wheel is moved."""
        numDegrees = event.angleDelta().y() / 8
        numSteps = numDegrees / 32
        self.zoom(pow(ZoomInFactor, numSteps))

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.lastDragPos = event.position()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.offset += event.position() - self.lastDragPos
            self.lastDragPos = event.position()
            self.update()

    def zoom(self, zoomFactor):
        """Zoom the mapView and keep mouse in the same spot."""
        self.scale *= zoomFactor
        self.offset *= zoomFactor
        self.offset += QPointF(self.mapFromGlobal(QCursor.pos())) * (1 - zoomFactor)
        self.update()

    def zoomCenter(self, zoomFactor):
        self.scale *= zoomFactor
        self.offset *= zoomFactor
        self.offset += QPointF(self.windowWidth/2, self.windowHeight/2) * (1 - zoomFactor)
        self.update()

    def scroll(self, deltaX, deltaY):
        """Translate mapView."""
        self.offset += QPointF(deltaX, deltaY)
        self.update()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    widget = MapViewWidget()
    widget.show()
    r = app.exec()
    sys.exit(r)
