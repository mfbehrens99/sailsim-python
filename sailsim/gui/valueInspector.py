"""This module contains the class declaration for the ValueInspectorWidget."""

from math import pi, sqrt

from PySide6.QtWidgets import QTreeWidget

def toString(text):
    return f'{text:.4f}'.rstrip('0').rstrip('.')

class ValueInspectorWidget(QTreeWidget):
    """List Widget that displays the boat's values."""

    def viewFrame(self, frame):
        self.updateValueInspectorRow(self.topLevelItem(0), frame.boatPosX, frame.boatPosY)

        self.topLevelItem(1).setText(1, toString(frame.boatDirection * 180 / pi))

        self.updateValueInspectorRow(self.topLevelItem(2), frame.boatSpeedX, frame.boatSpeedY)

        self.topLevelItem(3).setText(1, toString(frame.boatAngSpeed * 180 / pi))

        # Display Forces
        itemForce = self.topLevelItem(4)
        self.updateValueInspectorRow(itemForce, frame.boatForceX, frame.boatForceY)
        self.updateValueInspectorRow(itemForce.child(0), frame.boatSailDragX, frame.boatSailDragY)
        self.updateValueInspectorRow(itemForce.child(1), frame.boatSailLiftX, frame.boatSailLiftY)
        self.updateValueInspectorRow(itemForce.child(2), frame.boatCenterboardDragX, frame.boatCenterboardDragY)
        self.updateValueInspectorRow(itemForce.child(3), frame.boatCenterboardLiftX, frame.boatCenterboardLiftY)
        self.updateValueInspectorRow(itemForce.child(4), frame.boatRudderDragX, frame.boatRudderDragY)
        self.updateValueInspectorRow(itemForce.child(5), frame.boatRudderLiftX, frame.boatRudderLiftY)
        # self.updateValueInspectorRow(itemForce.child(6), frame.boatHullDragX, frame.boatHullDragY)
        # self.updateValueInspectorRow(itemForce.child(7), frame.boatHullLiftX, frame.boatHullLiftY)

        # Display Torque
        itemTorque = self.topLevelItem(5)
        itemTorque.setText(1, toString(frame.boatTorque))
        itemTorque.child(0).setText(1, toString(frame.boatWaterDragTorque))
        itemTorque.child(1).setText(1, toString(frame.boatCenterboardTorque))
        itemTorque.child(2).setText(1, toString(frame.boatRudderTorque))
        # itemTorque.child(3).setText(1, toString(frame.boatHullTorque))

        # Display Angles
        itemAngle = self.topLevelItem(6)
        itemAngle.child(0).setText(1, toString(frame.boatMainSailAngle))
        itemAngle.child(1).setText(1, toString(frame.boatRudderAngle))
        itemAngle.child(2).setText(1, toString(frame.boatLeewayAngle))


    def updateValueInspectorRow(self, item, valX, valY):
        item.setText(1, toString(sqrt(valX**2 + valY**2)))
        item.setText(2, toString(valX))
        item.setText(3, toString(valY))
