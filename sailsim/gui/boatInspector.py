"""This module contains the class declaration of BoatInspectorWidget."""

from os import path
from math import pi

from PySide6.QtCore import QPoint, Qt, QRectF, QPointF
from PySide6.QtGui import QColor, QPainter, QPixmap, QBrush, QImage
from PySide6.QtWidgets import QApplication, QWidget

BOAT_PATH = path.dirname(__file__) + "\\assets\\boat.png"


class BoatInspectorWidget(QWidget):
    """Display the state of the boat."""
    def __init__(self, parent=None):
        super(BoatInspectorWidget, self).__init__(parent)

        self.pixmap = QPixmap()
        self.pixmapOffset = QPoint()
        self.lastDragPos = QPoint()

        self.offset = QPoint(0, 0)
        self.radius = 0

        self.boatDirection = 0
        self.boatSpeed = QPointF(0, 0)


        self.setWindowTitle("BoatInspectorWidget")
        # self.setCursor(Qt.CrossCursor)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.translate(self.offset)
        painter.rotate(self.boatDirection)

        size = self.radius * 0.5
        width = 1.2 * size
        height = 4.2 * size
        target = QRectF(-width/2, -height/2, width, height)
        img = QImage(BOAT_PATH)
        painter.drawImage(target, img)

        col = QColor(0, 0, 0)
        painter.setPen(col)

        painter.setBrush(QBrush(QColor(200, 0, 0), Qt.NoBrush))
        painter.drawEllipse(QPoint(0, 0), self.radius, self.radius)

    def viewFrame(self, frame):
        """Set the boat to a position saved in a frame given."""
        self.boatDirection = frame.boatDirection / pi * 180
        self.update()

    def resizeEvent(self, event):
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
