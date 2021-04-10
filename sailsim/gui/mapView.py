"""PySide6 port of the corelib/threads/mandelbrot example from Qt v5.x, originating from PyQt"""

from math import pi

from PySide6.QtCore import Signal, QMutex, QMutexLocker, QPoint, QSize, Qt, QPointF, QRectF
from PySide6.QtGui import QColor, QPainter, QPen, QPainterPath, QCursor, QImage
from PySide6.QtWidgets import QApplication, QWidget

from sailsim.gui.drawBoat import DrawBoat


DefaultCenterX = 0
DefaultCenterY = 0
DefaultScale = 1

ZoomInFactor = 1.25
ZoomOutFactor = 1 / ZoomInFactor
ScrollStep = 10


def pointsToPath(points):
    path = QPainterPath()
    path.moveTo(QPointF(points[0][0], points[0][1]))
    for p in points[1:]:
        path.lineTo(QPointF(p[0],p[1]))
    return path



class MapViewWidget(QWidget):
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

        self.simulation = None

        self.setWindowTitle("MapViewWidget")
        self.setCursor(Qt.CrossCursor)
        self.resize(550, 400)


    def paintEvent(self, event):
        painter = QPainter(self)

        painter.translate(self.offset)
        painter.scale(self.scale, self.scale)

        painter.setPen(QPen(Qt.black, 4/self.scale, Qt.SolidLine, Qt.RoundCap, Qt. RoundJoin))
        painter.drawPath(self.path)

        painter.translate(self.boatPos)
        painter.rotate(self.boatDir)

        width = 1.2
        height = 4.2
        target = QRectF(-width/2,-height/2, width, height)
        img = QImage("C:/Users/mfbeh/Documents/GitHub/sailsim/sailsim/gui/boat.png")
        painter.drawImage(target, img);


    def setPath(self, path):
        self.path = path
        self.update()

    def viewFrame(self, frameNr):
        (posX, posY) = (self.simulation.frameList.frames[frameNr].boatPosX, self.simulation.frameList.frames[frameNr].boatPosY)
        direction = self.simulation.frameList.frames[frameNr].boatDirection
        print(direction)
        self.setBoat(posX, posY, direction)

    def setBoat(self, posX, posY, direction):
        self.boatPos = QPointF(posX, posY)
        self.boatDir = direction / pi * 180

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