"""This module calculates momenta for the boat class"""

from sailsim.utils.constants import DENSITY_AIR, DENSITY_WATER


def waterDragMomentum(self):
    c_w = 1.1
    # TODO use c_w
    # NOTE formula does not contain an area (but only a length)
    # print(self.angSpeed)
    return -1 / 4 * c_w * DENSITY_WATER * pow(self.length, 4) * pow(self.angSpeed, 2)


def rudderMomentum(self, boatSpeedSq):
    return self.length * 0.5 * self.waterLiftRudderScalar(boatSpeedSq)
