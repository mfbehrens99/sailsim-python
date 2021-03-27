"""PySide6 port of the corelib/threads/mandelbrot example from Qt v5.x, originating from PyQt"""

from PySide6.QtCore import Signal, QPoint, Qt
from PySide6.QtGui import QColor, QPainter, QPixmap, QBrush, QTransform, QImage
from PySide6.QtWidgets import QApplication, QWidget


class BoatInspectorWidget(QWidget):
    def __init__(self, parent=None):
        super(BoatInspectorWidget, self).__init__(parent)

        self.pixmap = QPixmap()
        self.pixmapOffset = QPoint()
        self.lastDragPos = QPoint()

        self.centerX = 0
        self.centerY = 0
        self.radius = 0


        self.setWindowTitle("BoatInspectorWidget")
        # self.setCursor(Qt.CrossCursor)

    def paintEvent(self, event):
        painter = QPainter(self)

        self.pixmap = QPixmap()
        painter.drawPixmap(self.pixmapOffset, self.pixmap)

        # trans = QTransform().rotate(60)
        # painter.drawPixmap(0, 0, boat.transformed(trans))
        # painter.drawImage(QPoint(0, 0))

        col = QColor(0, 0, 0)
        painter.setPen(col)

        painter.setBrush(QBrush(QColor(200, 0, 0), Qt.NoBrush))
        painter.drawEllipse(QPoint(self.centerX, self.centerY), self.radius, self.radius)



    def resizeEvent(self, event):
        self.centerX = event.size().width() // 2
        self.centerY = event.size().height() // 2
        self.radius = min(event.size().width(), event.size().height()) // 2
        self.update()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    widget = BoatInspectorWidget()
    widget.show()
    r = app.exec_()
    sys.exit(r)
