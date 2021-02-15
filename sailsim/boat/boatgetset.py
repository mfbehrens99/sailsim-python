from math import pi

from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval


def getPos(self):
    """Return coordinates of the boat."""
    return (self.posX, self.posY)


def getSpeed(self):
    """Return boat speed components."""
    return (self.speedX, self.speedY)


def setDirection(self, direction):
    """Map direction into valid range and save."""
    self.direction = directionKeepInterval(direction)


def setMainSailAngle(self, mainSailAngle):
    """Map angle into valid range and save."""
    self.mainSailAngle = angleKeepInterval(mainSailAngle)


def setMainSailAngleDeg(self, mainSailAngle):
    """Convert degrees to radiants and run setMainSailAngle()."""
    self.setMainSailAngle(mainSailAngle * pi / 180)


def setConstants(self, mass, sailArea, hullArea, centerboardArea):
    """Define mass, sailArea, hullArea and centerboardArea (in kg, m^2)."""
    self.mass = mass
    self.sailArea = sailArea
    self.hullArea = hullArea
    self.centerboardArea = centerboardArea
