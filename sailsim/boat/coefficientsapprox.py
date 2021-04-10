"""These are approximated coefficient for sail boats."""

from math import pi


def coefficientAirDrag(angleOfAttack):
    """Calculate the wind resitance coefficient based on the angle of attack."""
    return 0.41 * pow(angleOfAttack, 2) + 0.13 * abs(angleOfAttack) + 0.3


def coefficientAirLift(angleOfAttack):
    """Calculate the wind lift coefficient based on the angle of attack."""
    return -3.5 * 16 / pow(pi, 2) * pow((abs(angleOfAttack) - pi / 4), 2) + 3.5


def coefficientWaterDrag(angleOfAttack):
    """Calculate the water drag coefficient based on the angle of attack."""
    return coefficientAirDrag(angleOfAttack)


def coefficientWaterLift(angleOfAttack):
    """Calculate the water lift coefficient based on the angle of attack."""
    return coefficientAirLift(angleOfAttack)
