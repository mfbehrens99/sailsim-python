"""This module holdes some force calculation for the Boat class."""

from math import pi

from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval
from sailsim.utils.coordconversion import polarToCart
from sailsim.utils.constants import DENSITY_AIR, DENSITY_WATER


def leverSpeedVector(self, lever):
    """Calculate the speed vector at a certain point concidering the rotation."""
    (orbSpeedX, orbSpeedY) = polarToCart(self.angSpeed * lever, directionKeepInterval(self.direction + pi))
    return (-self.speedX + orbSpeedX, -self.speedY + orbSpeedY)


# Sail forces
def sailDrag(self, apparentWindSpeed, apparentWindNormX, apparentWindNormY):
    """Calculate the force that is created when wind blows against the boat."""
    scalarSailDrag = 0.5 * DENSITY_AIR * self.sailArea * apparentWindSpeed**2 * self.coefficientAirDrag(self.temp_angleOfAttack)
    return self.scalarToDragForce(scalarSailDrag, apparentWindNormX, apparentWindNormY)


def sailLift(self, apparentWindSpeed, apparentWindNormX, apparentWindNormY):
    """Calculate the lift force that is created when the wind changes its direction in the sail."""
    scalarSailLift = 0.5 * DENSITY_AIR * self.sailArea * apparentWindSpeed**2 * self.coefficientAirLift(self.temp_angleOfAttack)
    return self.scalarToLiftForce(scalarSailLift, self.temp_angleOfAttack, apparentWindNormX, apparentWindNormY)


# Centerboard forces
def centerboardDrag(self, flowSpeedSq, flowSpeedCenterboardNormX, flowSpeedCenterboardNormY):
    """Calculate the drag force of the water that is decelerating the boat."""
    scalarCenterboardDrag = 0.5 * DENSITY_WATER * self.centerboardArea * flowSpeedSq * self.coefficientWaterDrag(self.temp_leewayAngle)
    return self.scalarToDragForce(scalarCenterboardDrag, flowSpeedCenterboardNormX, flowSpeedCenterboardNormY)


def centerboardLift(self, flowSpeedSq, flowSpeedCenterboardNormX, flowSpeedCenterboardNormY):
    """Calculate force that is caused by lift forces in the water."""
    scalarCenterboardLift = 0.5 * DENSITY_WATER * self.centerboardArea * flowSpeedSq * self.coefficientWaterLift(self.temp_leewayAngle)
    return self.scalarToLiftForce(scalarCenterboardLift, self.temp_leewayAngle, flowSpeedCenterboardNormX, flowSpeedCenterboardNormY)


# Rudder forces
def rudderDrag(self, flowSpeedSq, flowSpeedRudderNormX, flowSpeedRudderNormY):
    """Calculates Force of the rudder that ist decelerating the boat."""
    scalarRudderDrag = 0.5 * DENSITY_WATER * self.rudderArea * flowSpeedSq * self.coefficientWaterDrag(angleKeepInterval(self.temp_leewayAngle + self.rudderAngle))
    return self.scalarToDragForce(scalarRudderDrag, flowSpeedRudderNormX, flowSpeedRudderNormY)


def rudderLift(self, flowSpeedSq, flowSpeedRudderNormX, flowSpeedRudderNormY):
    """Calculates Lift caused by rudder."""
    scalarRudderLift = 0.5 * DENSITY_WATER * self.rudderArea * flowSpeedSq * self.coefficientWaterLift(angleKeepInterval(self.temp_leewayAngle + self.rudderAngle))
    return self.scalarToLiftForce(scalarRudderLift, angleKeepInterval(self.temp_leewayAngle + self.rudderAngle), flowSpeedRudderNormX, flowSpeedRudderNormY)




# Conversions
def scalarToLiftForce(self, scalarForce, angleOfAttack, normX, normY):
    """Convert scalar lift force into cartesian vector"""
    if angleOfAttack < 0:
        return (-scalarForce * normY, scalarForce * normX)    # rotate by 90° counterclockwise
    return (scalarForce * normY, -scalarForce * normX)        # rotate by 90° clockwise


def scalarToDragForce(self, scalarForce, normX, normY):
    """Convert scalar drag force into cartesian vector"""
    return (scalarForce * normX, scalarForce * normY)
