"""Contains modules for GUI elements"""

from math import acos, cos, pi, sin, atan2
from functools import cached_property

from PySide6.QtCore import QPoint, QPointF, QLine, QLineF, QRect, QRectF, QSize
from PySide6.QtGui import QBrush, QPainterPath, QPen, QPolygonF, Qt
from PySide6.QtWidgets import QGraphicsItem, QGraphicsLineItem, QGraphicsPathItem


class GUIBoat(QGraphicsItem):
    mainSail = QLineF(0, 0, 0, 2)
    rudder = QLineF(0, 2.2, 0, 2.2)

    displayMainSail = True
    displayRudder = True
    displayPath = True
    displayForces = True

    def __init__(self, boat, parent=None):
        """Creates a GUIBoat Objects.

        Args:
            boat:   Boat to display
            parent: Parent of the QGraphicsItem"""
        super().__init__(parent)
        self.frameList = boat.frameList

    def paint(self, painter, _option, _widget):
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.black)
        painter.drawPath(self.boatShape)
        painter.setBrush(Qt.NoBrush)
        if self.displayMainSail:
            painter.setPen(QPen(Qt.green, 0.1, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(self.mainSail)
        if self.displayRudder:
            painter.setPen(QPen(Qt.blue, 0.1, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(self.rudder)

    def boundingRect(self):
        return self.boatShape.boundingRect() | QRectF(self.mainSail.p1(), self.mainSail.p2()) | QRectF(self.rudder.p1(), self.rudder.p2())

    @cached_property
    def boatShape(self) -> QPainterPath:
        """Return the QPainterPath for drawing a boat."""
        boat = QPainterPath()
        boat.moveTo(0, -2)
        boat.cubicTo(QPointF(1, -.5), QPointF(1, .5), QPointF(.8, 2.2))
        boat.lineTo(-.8, 2.2)
        boat.cubicTo(QPointF(-1, .5), QPointF(-1, -.5), QPointF(0, -2))
        return boat

    def setFrame(self, framenumber):
        """Load frame x from the framelist.

        Args:
            framenumber:int   number of the frame"""
        frame = self.frameList[framenumber]
        self.setPos(QPointF(frame.boatPosX, -frame.boatPosY))
        self.setRotation(frame.boatDirection / pi * 180)

        self.mainSail.setP2(QPointF(-sin(frame.boatMainSailAngle), cos(frame.boatMainSailAngle)) * 2)
        self.rudder.setP2(self.rudder.p1() + QPointF(sin(frame.boatRudderAngle), cos(frame.boatRudderAngle)) * 0.5)


class QGraphicsArrowItem(QGraphicsLineItem):
    arrowHead = None
    def __init__(self, *args):
        super().__init__(*args)
        self._brush = QBrush(self.pen().color())
        self.updatedHead()

    def shape(self):
        path = super().shape()
        path.addPolygon(self.arrowHead)
        return path

    def updatePosition(self):
        line = QLineF(self.mapFromItem(self.myStartItem, 0, 0), self.mapFromItem(self.myEndItem, 0, 0))
        self.setLine(line)

    def updatedHead(self):
        line = self.line()
        angle = atan2(line.dy(), line.dx())
        arrowAngle = .3
        point1 = line.p2() + QPointF(cos(pi/2 - angle - arrowAngle), sin(pi/2 - angle - arrowAngle)) * 10
        point2 = line.p2() + QPointF(cos(pi/2 - angle + arrowAngle), sin(pi/2 - angle + arrowAngle)) * 10
        self.arrowHead = QPolygonF([point1, line.p2(), point2])

    def setLine(self, line):
        self.updateHead()
        super().setLine(line)

    def setBrush(self, brush):
        self._brush = brush

    def brush(self):
        return self._brush

    def paint(self, painter, option, widget=None):
        super().paint(painter, option, widget)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush)
        painter.drawPolygon(self.arrowHead)


def pointsToPath(points, jump=1):
    """Convert a pointlist into a QPainterPath."""
    path = QPainterPath()
    path.moveTo(QPointF(points[0][0], -points[0][1]))
    for i in range(0, len(points), jump)[1:]:
        point = points[i]
        path.lineTo(QPointF(point[0], -point[1]))
    return path


class GUIPath(QGraphicsPathItem):
    def __init__(self, boat, *args):
        super().__init__(*args)
        self.frameList = boat.frameList
        self.updateBoatPath(5)

    def updateBoatPath(self, jump=1):
        """Convert a pointlist into a QPainterPath."""
        points = self.frameList.getCoordinateList()
        self.setPath(pointsToPath(points, jump))

    def paint(self, painter, *args):
        transform = painter.transform()
        scale = min(transform.m11(), transform.m22())
        pen = self.pen()
        pen.setWidthF(self.pen().widthF() / scale)
        painter.setPen(pen)
        painter.drawPath(self.path())


class BoatVectors(QGraphicsItem):
    boatSpeed = QPointF(0, 0)
    boatForce = QPointF(0, 0)

    boatForceSailDrag = QPointF(0, 0)
    boatForceSailLift = QPointF(0, 0)
    boatForceCenterboardDrag = QPointF(0, 0)
    boatForceCenterboardLift = QPointF(0, 0)
    boatForceRudderDrag = QPointF(0, 0)
    boatForceRudderLift = QPointF(0, 0)
    boatRudderPosition = QPointF(0, 0)

    def __init__(self, boat, parent) -> None:
        super().__init__(parent)
        self.frameList = boat.frameList

    def paint(self, painter):
        scaleSpeed = 8
        scaleForce = 1 / 2048
        painter.scale(1/4, 1/4)

        # Display Direction and Speed
        painter.setPen(Qt.blue)
        painter.drawLine(QPoint(0, 0), self.boatSpeed * scaleSpeed)

        painter.setPen(Qt.darkRed)
        painter.drawLine(QPoint(0, 0), self.boatForce * scaleForce)
        painter.setPen(Qt.red)
        painter.drawLine(QPoint(0, 0), self.boatForceSailDrag * scaleForce)
        painter.drawLine(QPoint(0, 0), self.boatForceSailLift * scaleForce)
        painter.drawLine(QPoint(0, 0), self.boatForceCenterboardDrag * scaleForce)
        painter.drawLine(QPoint(0, 0), self.boatForceCenterboardLift * scaleForce)
        painter.drawLine(self.boatRudderPosition, self.boatRudderPosition+self.boatForceRudderDrag * scaleForce*4)
        painter.drawLine(self.boatRudderPosition, self.boatRudderPosition+self.boatForceRudderLift * scaleForce*4)
        painter.scale(4, 4)

    def setFrame(self, framenumber):
        frame = self.frameList[framenumber]
        self.boatSpeed = QPointF(frame.boatSpeedX, -frame.boatSpeedY)
        self.boatForce = QPointF(frame.boatForceX, -frame.boatForceY)

        self.boatForceSailDrag = QPointF(frame.boatSailDragX, -frame.boatSailDragY)
        self.boatForceSailLift = QPointF(frame.boatSailLiftX, -frame.boatSailLiftY)
        self.boatForceCenterboardDrag = QPointF(frame.boatCenterboardDragX, -frame.boatCenterboardDragY)
        self.boatForceCenterboardLift = QPointF(frame.boatCenterboardLiftX, -frame.boatCenterboardLiftY)
        self.boatForceRudderDrag = QPointF(frame.boatRudderDragX, -frame.boatRudderDragY)
        self.boatForceRudderLift = QPointF(frame.boatRudderLiftX, -frame.boatRudderLiftY)
        self.boatRudderPosition = QPointF(-sin(frame.boatDirection)*2.2, cos(frame.boatDirection)*2.2)
