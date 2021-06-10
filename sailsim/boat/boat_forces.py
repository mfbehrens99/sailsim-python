"""This module holdes some force calculation for the Boat class."""

from math import sin

from sailsim.utils.anglecalculations import angleKeepInterval
from sailsim.utils.constants import DENSITY_AIR, DENSITY_WATER


# Sail forces
def sailDrag(self, apparentWindSpeedSq):
    """Calculate the force that is created when wind blows against the boat."""
    return 0.5 * DENSITY_AIR * self.sailArea * apparentWindSpeedSq * self.coefficientAirDrag(self.dataHolder.angleOfAttack)


def sailLift(self, apparentWindSpeedSq):
    """Calculate the lift force that is created when the wind changes its direction in the sail."""
    return 0.5 * DENSITY_AIR * self.sailArea * apparentWindSpeedSq * self.coefficientAirLift(self.dataHolder.angleOfAttack)


# Hull forces
def waterDrag(self, boatSpeedSq):
    """Calculate the drag force of the water that is decelerating the boat."""
    return -0.5 * DENSITY_WATER * (self.hullArea + self.centerboardArea) * boatSpeedSq * self.coefficientWaterDrag(self.dataHolder.leewayAngle)


def waterLift(self, boatSpeedSq):
    """Calculate force that is caused by lift forces in the water."""
    return -0.5 * DENSITY_WATER * self.centerboardArea * boatSpeedSq * self.coefficientWaterLift(self.dataHolder.leewayAngle)


# Rudder forces
def waterLiftRudder(self, boatSpeedSq):
    """Calculates Lift caused by rudder."""
    return -0.5 * DENSITY_WATER * self.rudderArea * boatSpeedSq * self.coefficientWaterLift(angleKeepInterval(self.dataHolder.leewayAngle + self.rudderAngle))


def waterDragRudder(self, boatSpeedSq):
    """Calculates Force of the rudder that ist decelerating the boat."""
    return -0.5 * DENSITY_WATER * self.rudderArea * boatSpeedSq * self.coefficientWaterDrag(angleKeepInterval(self.dataHolder.leewayAngle + self.rudderAngle))

# Conversions
def scalarToLiftForce(self, scalarForce, angleOfAttack, normX, normY):
    """Convert scalar lift force into cartesian vector"""
    if angleOfAttack < 0:
        return (-scalarForce * normY, scalarForce * normX)    # rotate by 90° counterclockwise
    return (scalarForce * normY, -scalarForce * normX)        # rotate by 90° clockwise


def scalarToDragForce(self, scalarForce, normX, normY):
    """Convert scalar drag force into cartesian vector"""
    return (scalarForce * normX, scalarForce * normY)
