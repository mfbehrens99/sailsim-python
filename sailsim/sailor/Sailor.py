from math import pi

from sailsim.utils.coordconversion import polarToCart, cartToArg
from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval

from sailsim.sailor.Commands import Waypoint  # , Command


class Sailor:
    """Calculate mainSailAngle and mainRudderAngle."""

    from .sailorgetset import setCommandList, configBoat, configSailor, importBoat

    destX: float = 0
    destY: float = 0
    commandListIndex: int = 0

    rudderAngle: float
    boatDirection: float

    mainSailAngle: float

    mass: float
    sailArea: float
    hullArea: float
    centerboardArea: float

    maxMainSailAngle: float
    maxRudderAngle: float

    tackingAngleUpwind: float
    tackingAngleDownwind: float

    def __init__(self, commandList: list[Waypoint]) -> None:
        """
        Create a Sailor for steering a Boat.

        Args:
            commandList:    List of command objects from sailsim.sailor.Commands
        """
        self.commandList = commandList

        self.tackingAngleBufferSize = 10 / 180 * pi

    def run(self, posX: float, posY: float, gpsSpeed: float, gpsDir: float, compass: float, windSpeed: float, windAngle: float) -> None:
        """Execute Sailor calculations and save results in object properties."""
        self.checkCommand(posX, posY)

        straightCourse = cartToArg(self.destX - posX, self.destY - posY)
        trueWindDir = trueWindDirection(gpsSpeed, gpsDir, windSpeed, directionKeepInterval(windAngle + compass))
        windCourseAngle = angleKeepInterval(trueWindDir - straightCourse)

        leewayAngle = angleKeepInterval(gpsDir - compass)

        # reachable in a straight line ?
        if abs(windCourseAngle) > pi - self.tackingAngleUpwind - self.tackingAngleBufferSize:
            # upwind tacking
            llp = directionKeepInterval(trueWindDir + self.tackingAngleUpwind + pi)
            lln = directionKeepInterval(trueWindDir - self.tackingAngleUpwind + pi)
            if abs(angleKeepInterval(llp - straightCourse)) < self.tackingAngleBufferSize:
                self.boatDirection = llp
            elif abs(angleKeepInterval(lln - straightCourse)) < self.tackingAngleBufferSize:
                self.boatDirection = lln
            else:
                # choose closest layline
                if angleKeepInterval(trueWindDir - compass) > 0:
                    self.boatDirection = llp
                else:
                    self.boatDirection = lln
        elif abs(windCourseAngle) < angleKeepInterval(self.tackingAngleDownwind + self.tackingAngleBufferSize) and False:
            # downwind tacking
            # TODO implement downwind tacking
            pass
        else:
            # TODO improve leeway calculation
            self.boatDirection = straightCourse - (leewayAngle if abs(leewayAngle) < 0.5 else 0)

        offset = angleKeepInterval(self.boatDirection - compass)
        self.rudderAngle = offset * 0.5 / gpsSpeed if gpsSpeed != 0 else 0.00000001

        # Prevent sailor from oversteering
        if abs(self.rudderAngle) > self.maxRudderAngle:
            if self.rudderAngle > 0:
                self.rudderAngle = self.maxRudderAngle
            else:
                self.rudderAngle = -self.maxRudderAngle

        # NOTE this is a very simple approximation of the real curve
        self.mainSailAngle = angleKeepInterval((windAngle - pi)) / 2

    def checkCommand(self, posX: float, posY: float) -> None:
        """Execute commands from commandList."""
        # TODO make prettier
        while len(self.commandList) > self.commandListIndex:
            success = None
            command = self.commandList[self.commandListIndex]
            if isinstance(command, Waypoint):
                success = command.checkWaypoint(self, posX, posY)
            # elif isinstance(command, Command):
            #     pass # TODO run Command

            # If command was run successfully run next command, if not continue sailing
            if success:
                self.commandListIndex += 1
            else:
                return

    def setDestination(self, destX: float, destY: float) -> None:
        """Set Sailor's destination to specific coordinates."""
        self.destX = destX
        self.destY = destY


def trueWindDirection(gpsSpeed: float, gpsDir: float, windSpeed: float, windAngle: float) -> float:
    """Calculate trueWindDirection from gps and wind measurement."""
    (gpsX, gpsY) = polarToCart(gpsSpeed, gpsDir)
    (windX, windY) = polarToCart(windSpeed, windAngle)
    return cartToArg(gpsX + windX, gpsY + windY)
