"""
This module is converting Cartesian coordinates into polar coordinates and vice versa.

All angles are in radiants and between 0 and 2*pi.
The argument is measured clockwise between the positive y-axis and the vector like it can be
found on a compass. So this definition differs from the standard definition of angles in mathematics.
"""

from math import sin, cos, atan, pi, sqrt


def cartToRadius(cartX, cartY):
    """Convert Cartesian coordinates into their corresponding radius."""
    return sqrt(cartX**2 + cartY**2)


def cartToRadiusSq(cartX, cartY):
    """Convert Cartesian coordinates into their corresponding radius squared."""
    return cartX**2 + cartY**2


def cartToArg(cartX, cartY):
    """Convert Cartesian coordinates into their corresponding argument (angle)."""
    if cartY != 0: # Don't divide by 0
        if cartY < 0:               # 2nd and 3rd quadrant
            return atan(cartX / cartY) + pi
        if cartX < 0:               # 4st quadrant
            return atan(cartX / cartY) + 2 * pi
        return atan(cartX / cartY)  # else 1th quadrant
    if cartX > 0:
        return pi / 2               # 90 degrees
    if cartX == 0:
        return 0                    # 0 degrees when speed is 0
    return 3 / 2 * pi               # 270 degrees


def cartToPolar(cartX, cartY):
    """Convert Cartesian coordinates into polar coordinates."""
    return (cartToRadius(cartX, cartY), cartToArg(cartX, cartY))


def polarToCart(radius, argument):
    """Convert polar coordinates into Cartesian coordinates."""
    cartX = radius * sin(argument)
    cartY = radius * cos(argument)
    return (cartX, cartY)
