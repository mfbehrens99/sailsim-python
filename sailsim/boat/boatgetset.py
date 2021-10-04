from math import pi

from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval


def setBoat(self, posX, posY, direction=0, speedX=0, speedY=0, angSpeed=0):
    """Set important properties of boat."""
    self.posX = posX
    self.posY = posY
    self.direction = direction
    self.speedX = speedX
    self.speedY = speedY
    self.angSpeed = angSpeed


def getPos(self):
    """Return coordinates of the boat."""
    return (self.posX, self.posY)


def getSpeed(self):
    """Return boat speed components."""
    return (self.speedX, self.speedY)


def setDirection(self, direction):
    """Map direction into valid range and save."""
    self.direction = directionKeepInterval(direction)


def setDirectionDeg(self, direction):
    """Map direction into valid range and save."""
    self.direction = direction * pi / 180


def setMainSailAngle(self, mainSailAngle):
    """Map angle into valid range and save."""
    self.mainSailAngle = angleKeepInterval(mainSailAngle)


def setMainSailAngleDeg(self, mainSailAngle):
    """Convert degrees to radiants and run setMainSailAngle()."""
    self.setMainSailAngle(mainSailAngle * pi / 180)


def setRudderAngle(self, rudderAngle):
    """Map angle into valid range and save."""
    self.rudderAngle = angleKeepInterval(rudderAngle)


def setRudderAngleDeg(self, rudderAngle):
    """Convert degrees to radiants and run setRudderAngle()."""
    self.setRudderAngle(rudderAngle * pi / 180)


def setConstants(self, mass, sailArea, hullArea, centerboardArea):
    """Define mass, sailArea, hullArea and centerboardArea (in kg, m^2)."""
    self.mass = mass
    self.sailArea = sailArea
    self.hullArea = hullArea
    self.centerboardArea = centerboardArea
