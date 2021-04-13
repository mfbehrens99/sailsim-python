"""This module holdes some force calculation for the Boat class."""

from math import sin

from sailsim.utils.anglecalculations import angleKeepInterval
from sailsim.utils.constants import DENSITY_AIR, DENSITY_WATER


# Sail forces
def sailDrag(self, apparentWindNormX, apparentWindNormY, apparentWindSpeedSq):
    """Calculate the force that is created when wind blows against the boat."""
    force = 0.5 * DENSITY_AIR * self.sailArea * apparentWindSpeedSq * self.coefficientAirDrag(self.dataHolder.angleOfAttack)
    return (force * apparentWindNormX, force * apparentWindNormY)


def sailLift(self, apparentWindNormX, apparentWindNormY, apparentWindSpeedSq):
    """Calculate the lift force that is created when the wind changes its direction in the sail."""
    force = 0.5 * DENSITY_AIR * self.sailArea * apparentWindSpeedSq * self.coefficientAirLift(self.dataHolder.angleOfAttack)
    if self.dataHolder.angleOfAttack < 0:
        return (-force * apparentWindNormY, force * apparentWindNormX)  # rotate by 90° counterclockwise
    return (force * apparentWindNormY, -force * apparentWindNormX)      # rotate by 90° clockwise


# Hull forces
def waterDrag(self, speedNormX, speedNormY, boatSpeedSq):
    """Calculate the drag force of the water that is decelerating the boat."""
    force = -0.5 * DENSITY_WATER * (self.hullArea + self.centerboardArea) * boatSpeedSq * self.coefficientWaterDrag(self.dataHolder.leewayAngle)
    return (force * speedNormX, force * speedNormY) # TODO waterDrag


def waterLift(self, speedNormX, speedNormY, boatSpeedSq):
    """Calculate force that is caused by lift forces in the water."""
    force = -0.5 * DENSITY_WATER * self.centerboardArea * boatSpeedSq * self.coefficientWaterLift(self.dataHolder.leewayAngle)
    if self.dataHolder.leewayAngle < 0:
        return (-force * speedNormY, force * speedNormX)    # rotate by 90° counterclockwise
    return (force * speedNormY, -force * speedNormX)        # rotate by 90° clockwise


# Rudder forces
def waterDragRudder(self, speedNormX, speedNormY, boatSpeedSq):
    force = self.waterDragRudderScalar(boatSpeedSq)
    return (force * speedNormX, force * speedNormY)


def waterLiftRudder(self, speedNormX, speedNormY, boatSpeedSq):
    force = self.waterLiftRudderScalar(boatSpeedSq)
    return (force * speedNormY, -force * speedNormX)


def waterLiftRudderScalar(self, boatSpeedSq):
    force = -0.5 * DENSITY_WATER * self.rudderArea * boatSpeedSq * self.coefficientWaterLift(angleKeepInterval(self.dataHolder.leewayAngle + self.rudderAngle))
    if angleKeepInterval(self.dataHolder.leewayAngle + self.rudderAngle) < 0:
        return force
    return -force


def waterDragRudderScalar(self, boatSpeedSq):
    return -0.5 * DENSITY_WATER * self.rudderArea * boatSpeedSq * self.coefficientWaterDrag(angleKeepInterval(self.dataHolder.leewayAngle + self.rudderAngle))
