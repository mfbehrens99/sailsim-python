"""This module is intended for angle and direction calculations."""

from numpy import pi


def angleKeepInterval(angle: float) -> float:
    """Keep angle inside the range of (-pi; pi]."""
    if -pi < angle <= pi:
        return angle
    return (angle + pi) % (2 * pi) - pi


def directionKeepInterval(direction: float) -> float:
    """Keep direction inside the range of [0; 2*pi)."""
    return direction % (2 * pi)
