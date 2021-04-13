"""This module contains the class declaration for the MapViewWidget."""

from math import pi, sin, cos

from PySide6.QtCore import QPoint, QPointF, Qt
from PySide6.QtGui import QCursor, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import QApplication, QWidget

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


def boatPainterPath():
    """Return the QPainterPath for drawing a boat."""
    boat = QPainterPath()
    boat.moveTo(0, -2)
    boat.cubicTo(QPointF(1, -.5), QPointF(1, .5), QPointF(.8, 2.2))
    boat.lineTo(-.8, 2.2)
    boat.cubicTo(QPointF(-1, .5), QPointF(-1, -.5), QPointF(0, -2))
    return boat


class MapViewWidget(QWidget):
    """Map Widget that displays the boat and its path."""

    windowWidth = 0
    windowHeight = 0

    offset = QPoint()
    scale = 4
    lastDragPos = QPoint()

    path = QPainterPath()

    boatPos = QPointF(0, 0)
    boatDir = 0
    boatMainSailAngle = 0
    boatRudderAngle = 0

    def __init__(self, parent=None):
        super(MapViewWidget, self).__init__(parent)

        self.setWindowTitle("MapViewWidget")
        self.setCursor(Qt.CrossCursor)
        self.resize(550, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        painter.translate(self.offset)
        painter.scale(self.scale, self.scale)

        painter.setPen(QPen(Qt.darkGray, 4 / self.scale, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawPath(self.path)

        painter.translate(self.boatPos)
        painter.rotate(self.boatDir)

        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.black)
        painter.drawPath(boatPainterPath())
        painter.setPen(QPen(Qt.green, 0.1, Qt.SolidLine, Qt.RoundCap))
        painter.drawLine(QPointF(0, 0), QPointF(sin(self.boatMainSailAngle), cos(self.boatMainSailAngle)) * 2)
        painter.setPen(QPen(Qt.blue, 0.1, Qt.SolidLine, Qt.RoundCap))
        painter.drawLine(QPointF(0, 2.2), QPointF(sin(self.boatRudderAngle), cos(self.boatRudderAngle)) * 0.5 + QPointF(0, 2.2))

    def setPath(self, path):
        """Change the path and updates the painter."""
        self.path = path
        self.update()

    def viewFrame(self, frame):
        """Set the boat to a position saved in a frame given."""
        self.setBoat(frame.boatPosX, frame.boatPosY, frame.boatDirection, frame.boatMainSailAngle, frame.boatRudderAngle)

    def setBoat(self, posX, posY, direction, mainSailAngle, rudderAngle):
        """Set boat to a position given."""
        self.boatPos = QPointF(posX, -posY)
        self.boatDir = direction / pi * 180
        self.boatMainSailAngle = -mainSailAngle
        self.boatRudderAngle = rudderAngle
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
            self.zoom(ZoomInFactor)
        elif event.key() == Qt.Key_Minus:
            self.zoom(ZoomOutFactor)
        elif event.key() == Qt.Key_Left:
            self.scroll(+ScrollStep, 0)
        elif event.key() == Qt.Key_Right:
            self.scroll(-ScrollStep, 0)
        elif event.key() == Qt.Key_Down:
            self.scroll(0, -ScrollStep)
        elif event.key() == Qt.Key_Up:
            self.scroll(0, +ScrollStep)
        else:
            super(MapViewWidget, self).keyPressEvent(event)

    def wheelEvent(self, event):
        """Zoom in and out when mouse wheel is moved."""
        numDegrees = event.angleDelta().y() / 8
        numSteps = numDegrees / 32
        self.zoom(pow(ZoomInFactor, numSteps))

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.lastDragPos = QPoint(event.pos())

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.offset += event.pos() - self.lastDragPos
            self.lastDragPos = QPoint(event.pos())
            self.update()

    def zoom(self, zoomFactor):
        """Zoom the mapView and keep mouse in the same spot."""
        self.scale *= zoomFactor
        self.offset += (self.mapFromGlobal(QCursor.pos()) - self.offset) * (1 - zoomFactor)
        self.update()

    def scroll(self, deltaX, deltaY):
        """Translate mapView."""
        self.offset += QPoint(deltaX, deltaY)
        self.update()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    widget = MapViewWidget()
    widget.show()
    r = app.exec_()
    sys.exit(r)
