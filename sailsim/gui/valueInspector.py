"""This module contains the class declaration for the ValueInspectorWidget."""

from numpy import pi, sqrt

from PySide6.QtWidgets import QTreeWidget


def toString(text):
    """Convert numbers to string."""
    return f'{text:.4f}'.rstrip('0').rstrip('.')


class ValueInspectorWidget(QTreeWidget):
    """List Widget that displays the boat's values."""

    def viewFrame(self, frame):
        """Display values of a frame given in the value inspector."""
        self.updateValueInspectorRow(self.topLevelItem(0), frame.pose)
        self.topLevelItem(0).setText(3, toString(frame.pose[2] * 180 / pi))

        self.updateValueInspectorRow(self.topLevelItem(1), frame.speed)
        self.topLevelItem(1).setText(3, toString(frame.speed[2] * 180 / pi))

        # Display Forces
        itemForce = self.topLevelItem(2)
        self.updateValueInspectorRow(itemForce, frame.wrench)
        self.updateValueInspectorRow(itemForce.child(0), frame.wrenchSailDrag)
        self.updateValueInspectorRow(itemForce.child(1), frame.wrenchSailLift)
        self.updateValueInspectorRow(itemForce.child(2), frame.wrenchCenterboardDrag)
        self.updateValueInspectorRow(itemForce.child(3), frame.wrenchCenterboardLift)
        self.updateValueInspectorRow(itemForce.child(4), frame.wrenchRudderDrag)
        self.updateValueInspectorRow(itemForce.child(5), frame.wrenchRudderLift)
        # self.updateValueInspectorRow(itemForce.child(6), frame.wrenchHullDrag)
        # self.updateValueInspectorRow(itemForce.child(7), frame.wrenchHullLift)

        # Display Angles
        itemAngle = self.topLevelItem(3)
        itemAngle.child(0).setText(1, toString(frame.boatMainSailAngle))
        itemAngle.child(1).setText(1, toString(frame.boatRudderAngle))
        itemAngle.child(2).setText(1, toString(frame.boatLeewayAngle))


    def updateValueInspectorRow(self, item, wrench):
        item.setText(1, toString(wrench[0]))
        item.setText(2, toString(wrench[1]))
        item.setText(3, toString(wrench[2]))
