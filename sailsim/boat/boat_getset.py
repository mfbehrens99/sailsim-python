from numpy import pi, ndarray

from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval


def setBoat(self, pose: ndarray, speed: ndarray = ndarray([0, 0, 0])) -> float:
    """Set important properties of boat."""
    self.pose = pose
    self.speed = speed

def getPos(self) -> tuple[float, float]:
    """Return coordinates of the boat."""
    return (self.pose[0], self.pose[1])


def getSpeed(self) -> float:
    """Return boat speed components."""
    return (self.speedX, self.speedY)


def setDirection(self, direction: float) -> None:
    """Map direction into valid range and save."""
    self.direction = directionKeepInterval(direction)


def setDirectionDeg(self, direction: float) -> None:
    """Map direction into valid range and save."""
    self.direction = direction * pi / 180


def setMainSailAngle(self, mainSailAngle: float) -> None:
    """Map angle into valid range and save."""
    self.mainSailAngle = angleKeepInterval(mainSailAngle)


def setMainSailAngleDeg(self, mainSailAngle: float) -> None:
    """Convert degrees to radiants and run setMainSailAngle()."""
    self.setMainSailAngle(mainSailAngle * pi / 180)


def setRudderAngle(self, rudderAngle: float) -> None:
    """Map angle into valid range and save."""
    self.rudderAngle = angleKeepInterval(rudderAngle)


def setRudderAngleDeg(self, rudderAngle: float) -> None:
    """Convert degrees to radiants and run setRudderAngle()."""
    self.setRudderAngle(rudderAngle * pi / 180)


def setConstants(self, mass: float, sailArea: float, hullArea: float, centerboardArea: float) -> None:
    """Define mass, sailArea, hullArea and centerboardArea (in kg, m^2)."""
    self.mass = mass
    self.sailArea = sailArea
    self.hullArea = hullArea
    self.centerboardArea = centerboardArea
