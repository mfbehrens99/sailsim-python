"""This module contains the class declaration for the MapViewWidget."""

from os import path
from math import pi, sin, cos

from PySide6.QtCore import QPoint, QPointF, Qt
from PySide6.QtGui import QBrush, QColor, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import QApplication, QWidget


DefaultCenterX = 0
DefaultCenterY = 0
DefaultScale = 1

ZoomInFactor = 1.25
ZoomOutFactor = 1 / ZoomInFactor
ScrollStep = 10

BOAT_PATH = path.dirname(__file__) + "\\assets\\boat.png"


def pointsToPath(points, jump=1):
    """Convert a pointlist into a QPainterPath."""
    path = QPainterPath()
    path.moveTo(QPointF(points[0][0], -points[0][1]))
    for i in range(0, len(points), jump)[1:]:
        point = points[i]
        path.lineTo(QPointF(point[0], -point[1]))
    return path


class MapViewWidget(QWidget):
    """Map Widget that displays the boat and its path."""

    def __init__(self, parent=None):
        super(MapViewWidget, self).__init__(parent)

        self.offset = QPoint()
        self.lastDragPos = QPoint()

        self.width = 0
        self.height = 0
        self.scale = 1
        self.lastDragPosition = QPoint()

        self.path = QPainterPath()

        self.boatPos = QPointF(0, 0)
        self.boatDir = 0
        self.boatMainSailAngle = 0
        self.boatRudderAngle = 0

        self.simulation = None

        self.setWindowTitle("MapViewWidget")
        self.setCursor(Qt.CrossCursor)
        self.resize(550, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBackground(QBrush(QColor(100, 100, 255), Qt.Dense1Pattern))

        painter.translate(self.offset)
        painter.scale(self.scale, self.scale)

        painter.setPen(QPen(Qt.black, 4/self.scale, Qt.SolidLine, Qt.RoundCap, Qt. RoundJoin))
        painter.drawPath(self.path)

        painter.translate(self.boatPos)
        painter.rotate(self.boatDir)

        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.black)
        boat = QPainterPath()
        boat.moveTo(0, -2)
        boat.cubicTo(QPointF(1, -.5), QPointF(1, .5), QPointF(.8, 2.2))
        boat.lineTo(-.8, 2.2)
        boat.cubicTo(QPointF(-1, .5), QPointF(-1, -.5), QPointF(0, -2))
        painter.drawPath(boat)
        painter.setPen(QPen(Qt.green, .1, Qt.SolidLine, Qt.RoundCap))
        painter.drawLine(QPointF(0, 0), QPointF(sin(self.boatMainSailAngle), cos(self.boatMainSailAngle)) * 2)
        painter.setPen(QPen(Qt.blue, .1, Qt.SolidLine, Qt.RoundCap))
        painter.drawLine(QPointF(0, 2.2), QPointF(sin(self.boatRudderAngle), cos(self.boatRudderAngle)) * .5 + QPointF(0, 2.2))

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
        self.width = event.size().width()
        self.height = event.size().height()

    def keyPressEvent(self, event):
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
        numDegrees = event.angleDelta().y() / 8
        numSteps = numDegrees / 15.0
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
        self.scale *= zoomFactor
        # mouse = (self.mapFromGlobal(QCursor.pos()) - self.offset) / self.scale
        # self.offset -= QPoint(self.width // 2 * zoomFactor, self.height // 2 * zoomFactor)
        # print(self.offset.x(), self.offset.y())
        self.update()

    def scroll(self, deltaX, deltaY):
        self.offset += QPoint(deltaX, deltaY)
        self.update()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    widget = MapViewWidget()
    widget.show()
    r = app.exec_()
    sys.exit(r)
