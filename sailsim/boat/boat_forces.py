"""This module holdes some force calculation for the Boat class."""

from numpy import pi, ndarray, array, sin

from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval
from sailsim.utils.coordconversion import polarToCart
from sailsim.utils.constants import DENSITY_AIR, DENSITY_WATER
from sailsim.utils import Wrench


def leverSpeedVector(self, lever: float) -> ndarray:
    """Calculate the speed vector at a certain point considering the rotation."""
    (orbSpeedX, orbSpeedY) = polarToCart(self.speed[2] * lever, directionKeepInterval(self.pose[2] + pi))
    return array([-self.speed[0] + orbSpeedX, -self.speed[1] + orbSpeedY])


# Sail forces
def sailDrag(self, apparentWindSpeed: float, apparentWindNorm: ndarray) -> Wrench:
    """Calculate the force that is created when wind blows against the boat."""
    scalarForce = 0.5 * DENSITY_AIR * self.sailArea * apparentWindSpeed**2 * self.coefficientAirDrag(self.temp_angleOfAttack)
    # print(scalarForce, end="\t")
    return Wrench.fromForceAndTorque(apparentWindNorm * scalarForce)
    # return self.scalarToDragForce(scalarSailDrag, apparentWindNormX, apparentWindNormY)


def sailLift(self, apparentWindSpeed: float, apparentWindNorm: ndarray) -> Wrench:
    """Calculate the lift force that is created when the wind changes its direction in the sail."""
    scalarForce: float = 0.5 * DENSITY_AIR * self.sailArea * apparentWindSpeed**2 * self.coefficientAirLift(self.temp_angleOfAttack)
    # print(scalarForce)
    return Wrench.fromForceAndTorque(self.scalarToLiftForce(scalarForce, self.temp_angleOfAttack, apparentWindNorm))
    # return self.scalarToLiftForce(scalarSailLift, self.temp_angleOfAttack, apparentWindNormX, apparentWindNormY)


# Centerboard forces
def centerboardDrag(self, flowSpeedSq: float, flowSpeedCenterboardNorm: ndarray, dirNorm: ndarray) -> Wrench:
    """Calculate the drag force of the water that is decelerating the boat."""
    scalarForce = 0.5 * DENSITY_WATER * self.centerboardArea * flowSpeedSq * self.coefficientWaterDrag(self.temp_leewayAngle)
    return Wrench.fromForceAndLever(flowSpeedCenterboardNorm * scalarForce, dirNorm * self.centerboardLever)
    # return self.scalarToDragForce(scalarCenterboardDrag, flowSpeedCenterboardNormX, flowSpeedCenterboardNormY)


def centerboardLift(self, flowSpeedSq: float, flowSpeedCenterboardNorm: ndarray, dirNorm: ndarray) -> Wrench:
    """Calculate force that is caused by lift forces in the water."""
    scalarForce = 0.5 * DENSITY_WATER * self.centerboardArea * flowSpeedSq * self.coefficientWaterLift(self.temp_leewayAngle)
    return Wrench.fromForceAndLever(self.scalarToLiftForce(scalarForce, self.temp_leewayAngle, flowSpeedCenterboardNorm), dirNorm * self.centerboardLever)


# Rudder forces
def rudderDrag(self, flowSpeedSq: float, flowSpeedRudderNorm: ndarray, dirNorm: ndarray) -> Wrench:
    """Calculates Force of the rudder that ist decelerating the boat."""
    scalarForce = 0.5 * DENSITY_WATER * self.rudderArea * flowSpeedSq * self.coefficientWaterDrag(angleKeepInterval(self.temp_leewayAngle + self.rudderAngle))
    return Wrench.fromForceAndLever(flowSpeedRudderNorm * scalarForce, dirNorm * self.rudderLever)


def rudderLift(self, flowSpeedSq: float, flowSpeedRudderNorm: ndarray, dirNorm: ndarray) -> Wrench:
    """Calculates Lift caused by rudder."""
    scalarForce = 0.5 * DENSITY_WATER * self.rudderArea * flowSpeedSq * self.coefficientWaterLift(angleKeepInterval(self.temp_leewayAngle + self.rudderAngle))
    return Wrench.fromForceAndLever(self.scalarToLiftForce(scalarForce, angleKeepInterval(self.temp_leewayAngle + self.rudderAngle), flowSpeedRudderNorm), dirNorm * self.rudderLever)


# Hull forces
def waterDrag(self) -> Wrench:
    """Calculate the wrench of the hull that is cause by drag forces in the water."""
    # TODO add Forces, better approximation
    c_w = 1.1
    draught = .3  # bad approximation...
    torque = 1 / 64 * c_w * draught * DENSITY_WATER * pow(self.length, 4) * pow(self.speed[2], 2)
    if self.speed[2] < 0:
        return torque
    return -torque


# Conversions
# TODO move his method somewhere. Could be a static method or a function
def scalarToLiftForce(self, scalarForce: float, angleOfAttack: float, norm: ndarray) -> ndarray:
    """Convert scalar lift force into Cartesian vector."""
    if sin(angleOfAttack) < 0:
        return array([-scalarForce * norm[1], scalarForce * norm[0]])   # rotate by 90° counterclockwise
    return array([scalarForce * norm[1], -scalarForce * norm[0]])       # rotate by 90° clockwise
