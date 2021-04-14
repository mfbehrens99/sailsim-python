"""This module contains the class declaration of BoatInspectorWidget."""

from math import pi

from PySide6.QtCore import QPoint, QPointF, Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QWidget

from sailsim.gui.mapView import boatPainterPath


class BoatInspectorWidget(QWidget):
    """Display the state of the boat."""

    scaleBoat = 1 / 4
    scaleSpeed = 8
    scaleForce = 1 / 2048

    boatSpeed = QPointF(0, 0)
    boatForce = QPointF(0, 0)

    boatForceSailDrag = QPointF(0, 0)
    boatForceSailLift = QPointF(0, 0)
    boatForceWaterDrag = QPointF(0, 0)
    boatForceWaterLift = QPointF(0, 0)

    displayBoat = True
    displayMainSail = True
    displayRudder = True
    displayBoatDirection = True
    displaySpeed = True
    displayForces = True

    def __init__(self, parent=None):
        super(BoatInspectorWidget, self).__init__(parent)

        self.offset = QPoint(0, 0)
        self.radius = 0

        self.boatDirection = 0

    def paintEvent(self, event):
        r = self.radius
        scaleBoat, scaleSpeed, scaleForce = self.scaleBoat * r, self.scaleSpeed * r, self.scaleForce * r

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        painter.translate(self.offset)
        painter.rotate(self.boatDirection)

        # (temporary) circle around boat
        painter.setPen(Qt.lightGray)
        painter.drawEllipse(QPoint(0, 0), self.radius, self.radius)

        if self.displayBoat:
            painter.scale(scaleBoat, scaleBoat)
            painter.setPen(Qt.NoPen)
            painter.setBrush(Qt.gray)
            painter.drawPath(boatPainterPath())
            painter.scale(1 / scaleBoat, 1 / scaleBoat)

        if self.displayBoatDirection:
            painter.setPen(Qt.green)
            painter.drawLine(QPoint(0, 0), QPoint(0, -scaleBoat * 4))

        # Draw Vectors
        painter.resetTransform()
        painter.translate(self.offset)
        if self.displaySpeed:
            painter.setPen(Qt.blue)
            painter.drawLine(QPoint(0, 0), self.boatSpeed * scaleSpeed)

        if self.displayForces:
            painter.setPen(Qt.darkRed)
            painter.drawLine(QPoint(0, 0), self.boatForce * scaleForce)
            painter.setPen(Qt.red)
            painter.drawLine(QPoint(0, 0), self.boatForceSailDrag * scaleForce)
            painter.drawLine(QPoint(0, 0), self.boatForceSailLift * scaleForce)
            painter.drawLine(QPoint(0, 0), self.boatForceWaterDrag * scaleForce)
            painter.drawLine(QPoint(0, 0), self.boatForceWaterLift * scaleForce)

    def viewFrame(self, frame):
        """Set the boat to a position saved in a frame given."""
        self.boatDirection = frame.boatDirection / pi * 180
        self.boatSpeed = QPointF(frame.boatSpeedX, -frame.boatSpeedY)

        self.boatForce = QPointF(frame.boatForceX, -frame.boatForceY)
        self.boatForceSailDrag = QPointF(frame.boatSailDragX, -frame.boatSailDragY)
        self.boatForceSailLift = QPointF(frame.boatSailLiftX, -frame.boatSailLiftY)
        self.boatForceWaterDrag = QPointF(frame.boatWaterDragX, -frame.boatWaterDragY)
        self.boatForceWaterLift = QPointF(frame.boatWaterLiftX, -frame.boatWaterLiftY)
        self.update()

    def resizeEvent(self, event):
        """Keep size of the boatInspector at maximum size."""
        self.offset = QPoint(event.size().width() // 2, event.size().height() // 2)
        self.radius = min(event.size().width(), event.size().height()) // 2
        self.update()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    widget = BoatInspectorWidget()
    widget.show()
    r = app.exec_()
    sys.exit(r)
