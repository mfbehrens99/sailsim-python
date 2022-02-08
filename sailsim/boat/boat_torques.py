"""This module calculates torques for the boat class."""

from sailsim.utils.constants import DENSITY_AIR, DENSITY_WATER


def waterDragTorque(self):
    c_w = 1.1
    draught = .3 # bad approximation...
    # TODO use c_w
    # print(self.angSpeed)
    torque = 1 / 64 * c_w * draught * DENSITY_WATER * pow(self.length, 4) * pow(self.angSpeed, 2)
    if self.angSpeed < 0:
        return torque
    return -torque


def centerboardTorque(self, centerboardX, centerboardY, dirNormX, dirNormY):
    return (centerboardY * dirNormX - centerboardX * dirNormY) * self.centerboardLever # negative cross product

def rudderTorque(self, rudderX, rudderY, dirNormX, dirNormY):
    return (rudderY * dirNormX - rudderX * dirNormY) * self.rudderLever # negative cross product
