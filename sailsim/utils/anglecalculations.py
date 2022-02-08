"""This module is intended for angle and direction calculations."""

from math import pi


def angleKeepInterval(angle: float) -> float:
    """Keep angle inside the range of (-pi; pi]."""
    if angle > pi:
        return angle - 2 * pi
    if angle <= -pi:
        return angle + 2 * pi
    return angle


def directionKeepInterval(direction: float) -> float:
    """Keep direction inside the range of [0; 2*pi)."""
    return direction % (2 * pi)
