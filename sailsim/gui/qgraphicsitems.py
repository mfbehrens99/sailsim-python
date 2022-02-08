"""Contains modules for GUI elements."""

from math import atan2, cos, pi, sin, sqrt
from functools import cached_property
from typing import Optional, Union

from PySide6.QtCore import QLineF, QPoint, QPointF, QRectF
from PySide6.QtGui import QPainter, QPainterPath, QPen, QPolygonF, Qt
from PySide6.QtWidgets import QGraphicsItem, QGraphicsLineItem, QGraphicsPathItem, QStyleOptionGraphicsItem, QWidget

from sailsim.boat.Boat import Boat
from sailsim.sailor.Commands import Waypoint


def painterScale(painter: QPainter) -> float:
    """Calculate the scale of a QPainter."""
    # TODO method appears to have issues
    return sqrt(painter.transform().m11()**2 + painter.transform().m22()**2)


def dynamicSizePen(pen: QPen, painter: QPainter) -> QPen:
    """Change the thickness of the pen depending of the zoom of the painter."""
    pen.setWidthF(pen.widthF() / painterScale(painter))
    return pen


def pointsToPath(points: list[tuple[float, float]], jump: int = 1) -> QPainterPath:
    """Convert a pointlist into a QPainterPath."""
    path = QPainterPath()
    path.moveTo(QPointF(points[0][0], -points[0][1]))
    for i in range(0, len(points), jump)[1:]:
        point = points[i]
        path.lineTo(QPointF(point[0], -point[1]))
    return path


class GUIBoat(QGraphicsItem):
    """Display a sailsim boat in a QGraphicsScene."""

    mainSail = QLineF(0, 0, 0, 2)
    rudder = QLineF(0, 2.2, 0, 2.2)

    allowMovement = True

    displayMainSail = True
    displayRudder = True

    def __init__(self, boat: Boat, parent=None) -> None:
        """
        Create a GUIBoat Objects.

        Args:
            boat:   Boat to display
            parent: Parent of the QGraphicsItem
        """
        super().__init__(parent)
        self.frameList = boat.frameList

    def paint(self, painter: QPainter, _option: QStyleOptionGraphicsItem, _widget: Optional[QWidget] = None) -> None:
        """Paint the boat on the painter given."""
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

        # Draw bounding rectangle (for testing)
        # painter.setPen(dynamicSizePen(QPen(Qt.black), painter))
        # painter.setBrush(Qt.NoBrush)
        # painter.drawRect(self.boundingRect())

    def boundingRect(self) -> QRectF:
        """Return bounding rect of the boat."""
        return (self.boatShape.boundingRect()
                | QRectF(self.mainSail.p1(), self.mainSail.p2()).normalized()
                | QRectF(self.rudder.p1(), self.rudder.p2()).normalized()
                )

    @cached_property
    def boatShape(self) -> QPainterPath:
        """Return the QPainterPath for drawing a boat."""
        boat = QPainterPath()
        boat.moveTo(0, -2)
        boat.cubicTo(QPointF(1, -.5), QPointF(1, .5), QPointF(.8, 2.2))
        boat.lineTo(-.8, 2.2)
        boat.cubicTo(QPointF(-1, .5), QPointF(-1, -.5), QPointF(0, -2))
        return boat

    def setFrame(self, framenumber: int) -> None:
        """
        Load frame x from the framelist.

        Args:
            framenumber: int   number of the frame
        """
        frame = self.frameList[framenumber]
        if self.allowMovement:
            self.setPos(QPointF(frame.boatPosX, -frame.boatPosY))
        self.setRotation(frame.boatDirection / pi * 180)

        self.mainSail.setP2(QPointF(-sin(frame.boatMainSailAngle), cos(frame.boatMainSailAngle)) * 2)
        self.rudder.setP2(self.rudder.p1() + QPointF(sin(frame.boatRudderAngle), cos(frame.boatRudderAngle)) * 0.5)


class QGraphicsArrowItem(QGraphicsLineItem):
    """Draws a arrow with head."""

    arrowHead: QPolygonF
    headSize = 10.0
    arrowAngle = .4

    def __init__(self, *args) -> None:
        """Create a QGraphicsArrowItem."""
        super().__init__(*args)

        self.updateHead()

    def paint(self, painter: QPainter, _option: QStyleOptionGraphicsItem, _widget: Optional[QWidget] = None) -> None:
        """Paint QGraphicsArrowItem on the painter given."""
        self.updateHead(self.headSize / painterScale(painter))

        # Don't draw arrow if it intersects with itself
        if self.arrowHead.containsPoint(self.line().p1(), Qt.OddEvenFill) or self.line().length() == 0:
            return

        # Draw arrow line
        painter.setPen(dynamicSizePen(self.pen(), painter))
        painter.drawLine(self.line())

        # Draw arrow head
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.pen().color())
        painter.drawPolygon(self.arrowHead)

        # Draw bounding rectangle (for testing)
        # painter.setPen(dynamicSizePen(self.pen(), painter))
        # painter.setBrush(Qt.NoBrush)
        # painter.drawRect(self.boundingRect())

    def boundingRect(self) -> QRectF:
        """Return the bounding rectangle of the QGraphicsArrowItem."""
        return super().boundingRect() | self.arrowHead.boundingRect()

    def updateHead(self, scale: float = 1.0) -> None:
        """Update shape and size of the arrow head."""
        line = self.line()
        angle = atan2(line.dy(), line.dx())

        line1 = QPointF(sin(pi/2 - angle - self.arrowAngle), cos(pi/2 - angle - self.arrowAngle))
        line2 = QPointF(sin(pi/2 - angle + self.arrowAngle), cos(pi/2 - angle + self.arrowAngle))
        self.arrowHead = QPolygonF([line.p2() - line1 * scale, line.p2(), line.p2() - line2 * scale])

    def setP2(self, point: Union[QPoint, QPointF]) -> None:
        """Set the end point of the QGraphicsArrowItem."""
        line = self.line()
        line.setP2(point)
        self.setLine(line)


class GUIBoatPath(QGraphicsPathItem):
    """Display the path of a sailsim boat in a QGraphicsScene."""

    def __init__(self, boat: Boat, *args) -> None:
        """Create a GUIBoatPath object."""
        super().__init__(*args)
        self.frameList = boat.frameList
        self.updateBoatPath(5)

    def updateBoatPath(self, jump: int = 1) -> None:
        """Convert a pointlist into a QPainterPath."""
        points = self.frameList.getCoordinateList()
        self.setPath(pointsToPath(points, jump))

    def paint(self, painter: QPainter, _option: QStyleOptionGraphicsItem, _widget: Optional[QWidget] = None) -> None:
        """Paint the boat path on the painter given."""
        painter.setPen(dynamicSizePen(self.pen(), painter))
        painter.drawPath(self.path())


class GUIBoatVectors(QGraphicsItem):
    """Display boat vectors of a sailsim boat in a QGraphicsScene."""

    boatSpeed = QGraphicsArrowItem()
    boatForce = QGraphicsArrowItem()

    boatForceSailDrag = QGraphicsArrowItem()
    boatForceSailLift = QGraphicsArrowItem()
    boatForceCenterboardDrag = QGraphicsArrowItem()
    boatForceCenterboardLift = QGraphicsArrowItem()
    boatForceRudderDrag = QGraphicsArrowItem()
    boatForceRudderLift = QGraphicsArrowItem()
    boatRudderPosition = QGraphicsArrowItem()

    followBoat = True

    def __init__(self, boat: Boat, parent=None) -> None:
        """Create a GUIBoatVectors object."""
        super().__init__(parent)

        self.frameList = boat.frameList

        self.boatSpeed.setPen(QPen(Qt.blue, 2))
        self.boatForce.setPen(QPen(Qt.darkRed, 2))

        redPen = QPen(Qt.red)
        self.boatForceSailDrag.setPen(redPen)
        self.boatForceSailLift.setPen(redPen)
        self.boatForceCenterboardDrag.setPen(redPen)
        self.boatForceCenterboardLift.setPen(redPen)
        self.boatForceRudderDrag.setPen(redPen)
        self.boatForceRudderLift.setPen(redPen)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[QWidget] = None) -> None:
        """Paint boat Vectors with the painter given."""
        # Draw forces
        self.boatForceSailDrag.paint(painter, option, widget)
        self.boatForceSailLift.paint(painter, option, widget)

        self.boatForceCenterboardDrag.paint(painter, option, widget)
        self.boatForceCenterboardLift.paint(painter, option, widget)

        self.boatForceRudderDrag.paint(painter, option, widget)
        self.boatForceRudderLift.paint(painter, option, widget)

        # Display Direction and Speed
        self.boatSpeed.paint(painter, option, widget)
        self.boatForce.paint(painter, option, widget)

        # Draw bounding rectangle (for testing)
        # painter.setPen(dynamicSizePen(QPen(Qt.black), painter))
        # painter.setBrush(Qt.NoBrush)
        # painter.drawRect(self.boundingRect())

    def boundingRect(self) -> QRectF:
        """Return bounding rectangle of the boat vectors."""
        return (self.boatSpeed.boundingRect() | self.boatForce.boundingRect()
                | self.boatForceSailDrag.boundingRect() | self.boatForceSailLift.boundingRect()
                | self.boatForceCenterboardDrag.boundingRect() | self.boatForceCenterboardLift.boundingRect()
                | self.boatForceRudderDrag.boundingRect() | self.boatForceRudderLift.boundingRect()
                )

    def setFrame(self, framenumber: int) -> None:
        """
        Load frame x from the framelist.

        Args:
            framenumber: int   number of the frame
        """
        frame = self.frameList[framenumber]

        scaleForce = 1 / 1024

        if self.followBoat:
            self.setPos(QPointF(frame.boatPosX, -frame.boatPosY))

        self.boatSpeed.setP2(QPointF(frame.boatSpeedX, -frame.boatSpeedY))
        self.boatForce.setP2(QPointF(frame.boatForceX, -frame.boatForceY) * scaleForce)

        self.boatForceSailDrag.setP2(QPointF(frame.boatSailDragX, -frame.boatSailDragY) * scaleForce)
        self.boatForceSailLift.setP2(QPointF(frame.boatSailLiftX, -frame.boatSailLiftY) * scaleForce)

        self.boatForceCenterboardDrag.setP2(QPointF(frame.boatCenterboardDragX, -frame.boatCenterboardDragY) * scaleForce)
        self.boatForceCenterboardLift.setP2(QPointF(frame.boatCenterboardLiftX, -frame.boatCenterboardLiftY) * scaleForce)

        rudderStartPoint = QPointF(-sin(frame.boatDirection)*2.2, cos(frame.boatDirection)*2.2)
        self.boatForceRudderDrag.setLine(QLineF(rudderStartPoint,
                                                rudderStartPoint + QPointF(frame.boatRudderDragX, -frame.boatRudderDragY) * scaleForce))
        self.boatForceRudderLift.setLine(QLineF(rudderStartPoint,
                                                rudderStartPoint + QPointF(frame.boatRudderLiftX, -frame.boatRudderLiftY) * scaleForce))


class GUIWaypoints(QGraphicsItem):
    """Display the sailors waypoints on the map."""

    waypoints: list[tuple[QPointF, float]]
    waypointPath: QPainterPath
    waypointsBoundingRect: QRectF

    displayWaypoints = True
    displayWaypointsPath = True

    def __init__(self, boat: Boat, parent=None) -> None:
        """Create a GUIWaypoints object."""
        super().__init__(parent)

        self.sailor = boat.sailor
        self.updateWaypoints()

    def paint(self, painter: QPainter, _option: QStyleOptionGraphicsItem, _widget: Optional[QWidget] = None) -> None:
        """Paint waypoints with the painter given."""
        # connection line
        if self.displayWaypointsPath:
            painter.setPen(dynamicSizePen(QPen(Qt.black, 2), painter))
            painter.drawPath(self.waypointPath)

        # waypoint circles
        if self.displayWaypoints:
            for waypoint, radius in self.waypoints:
                painter.setPen(dynamicSizePen(QPen(Qt.blue), painter))
                painter.drawEllipse(waypoint, radius, radius)

        # Draw bounding rectangle (for testing)
        # painter.setPen(dynamicSizePen(QPen(Qt.black), painter))
        # painter.setBrush(Qt.NoBrush)
        # painter.drawRect(self.boundingRect())

    def boundingRect(self) -> QRectF:
        """Return bounding rectangle of the waypoints."""
        return self.waypointsBoundingRect

    def updateWaypoints(self):
        """Display the waypoints in a commandList on mapView."""
        if self.sailor is None:
            return
        self.waypoints = []
        commands = self.sailor.commandList
        if len(commands) > 0:
            self.waypointPath = QPainterPath()
            self.waypointsBoundingRect = QRectF()
            # TODO find out boat starting coordinates
            waypointPathList = [[0, 0]]

            for command in commands:
                if isinstance(command, Waypoint):
                    self.waypoints.append((QPointF(command.destX, -command.destY), command.radius))
                    waypointPathList.append((command.destX, command.destY))
                    self.waypointsBoundingRect |= QRectF(command.destX - command.radius,
                                                         -command.destY - command.radius,
                                                         2 * command.radius,
                                                         2 * command.radius)
            self.waypointPath = pointsToPath(waypointPathList)
