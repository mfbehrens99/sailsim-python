"""These are approximated coefficient for sail boats."""


def coefficientAirDrag(angleOfAttack):
    """Calculate the wind resitance coefficient based on the angle of attack."""
    return 0.41 * pow(angleOfAttack, 2) + 0.13 * abs(angleOfAttack) + 0.3


def coefficientAirLift(angleOfAttack):
    """Calculate the wind lift coefficient based on the angle of attack."""
    # if abs(angleOfAttack) > 1.07:
    #     return -3.3 * angleOfAttack + 5.18
    # return 11 * pow(angleOfAttack, 4) - 22.46 * pow(abs(angleOfAttack), 3) + 7.39 * pow(angleOfAttack, 2) + 5.88 * abs(angleOfAttack)
    return -3.5 * 16 / pow(3.14159,2) * pow((abs(angleOfAttack) - 3.14159 / 4),2) + 3.5


def coefficientWaterDrag(angleOfAttack):
    """Calculate the water drag coefficient based on the angle of attack."""
    return coefficientAirDrag(angleOfAttack)


def coefficientWaterLift(angleOfAttack):
    """Calculate the water lift coefficient based on the angle of attack."""
    return coefficientAirLift(angleOfAttack)
