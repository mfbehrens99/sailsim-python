"""This module is intended for angle and direction calcualtions."""

from math import pi


def angleKeepInterval(angle):
    """Keep angle inside the range of (-pi; pi]."""
    if angle > pi:
        return angle - 2 * pi
    if angle <= -pi:
        return angle + 2 * pi
    return angle


def directionKeepInterval(direction):
    """Keep direction inside the range of [0; 2*pi)."""
    return direction % (2 * pi)
