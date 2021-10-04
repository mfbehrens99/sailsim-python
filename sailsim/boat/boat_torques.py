"""This module calculates torques for the boat class."""

from sailsim.utils.constants import DENSITY_AIR, DENSITY_WATER


def waterDragTorque(self):
    c_w = 1.1
    # TODO use c_w
    # NOTE formula does not contain an area (but only a length)
    # print(self.angSpeed)
    torque = 1 / 4 * c_w * DENSITY_WATER * pow(self.length, 4) * pow(self.angSpeed, 2)
    if self.angSpeed < 0:
        return torque
    return -torque


def rudderTorque(self, rudderX, rudderY, dirNormX, dirNormY):
    return (rudderY * dirNormX - rudderX * dirNormY) * self.rudderLever # negative cross product
