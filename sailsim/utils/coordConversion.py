"""
This module is converting Cartesian coordinates into polar coordinates and vice versa.

All angles are in radiants and between 0 and 2*pi.
The argument is measured clockwise between the positive y-axis and the vector like it can be
found on a compass. So this definition differs from the standard definition of angles in mathematics.
"""

from math import sin, cos, atan, pi, sqrt

def cartToRadius(cartX, cartY):
    """Converts Cartesian coordinates into their corresponding radius"""
    return sqrt(cartX**2 + cartY**2)

def cartToArg(cartX, cartY):
    """Converts Cartesian coordinates into their corresponding argument (angle)"""
    if cartY != 0: # Don't divide by 0
        return atan(cartX/cartY)
    if cartX >= 0:
        return pi/2 # 90  degrees
    return 3/2*pi   # 270 degrees

def cartToPolar(cartX, cartY):
    """Convert Cartesian coordinates into polar coordinates"""
    return (cartToRadius(cartX, cartY), cartToArg(cartX, cartY))

def polarToCart(radius, argument):
    """Convert polar coordinates into Cartesian coordinates"""
    cartX = radius * cos(argument)
    cartY = radius * sin(argument)
    return (cartX, cartY)
