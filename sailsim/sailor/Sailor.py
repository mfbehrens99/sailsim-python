from math import pi

from sailsim.utils.coordconversion import polarToCart, cartToArg
from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval

from sailsim.sailor.Commands import Waypoint  # , Command
from sailsim.sailor.FrameList import FrameList


class Sailor:
    """Calculate mainSailAngle and mainRudderAngle."""

    from .sailorgetset import setCommandList, configBoat, configSailor, importBoat

    frameList = []
    frameNr = 0

    destX = 0
    destY = 0
    commandListIndex = 0

    boatDirection = None
    rudderAngle = None

    mainSailAngle = None

    mass = None
    sailArea = None
    hullArea = None
    centerboardArea = None

    maxMainSailAngle = None
    maxRudderAngle = None

    tackingAngleUpwind = None
    tackingAngleDownwind = None

    def __init__(self, commandList):
        """
        Create a Sailor for steering a Boat.

        Args:
            commandList:    List of command objects from sailsim.sailor.Commands
        """
        self.commandList = commandList
        self.frameList = FrameList()

        self.tackingAngleBufferSize = 10 / 180 * pi

    def run(self, posX, posY, gpsSpeed, gpsDir, compass, windSpeed, windAngle):
        """Execute Sailor calculations and save resultes in object properties."""
        self.checkCommand(posX, posY)

        straightCourse = cartToArg(self.destX - posX, self.destY - posY)
        trueWindDir = trueWindDirection(gpsSpeed, gpsDir, windSpeed, directionKeepInterval(windAngle + compass))
        leewayAngle = angleKeepInterval(gpsDir - compass)

        windCourseAngle = angleKeepInterval(trueWindDir - straightCourse)

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
        self.rudderAngle = 0

        # Rudder main sail calculations
        # NOTE this is a very simple approximation of the real curve
        self.mainSailAngle = angleKeepInterval((windAngle - pi)) / 2

        # Save information to Frame
        self.addFrame(
            (posX, posY, gpsSpeed, gpsDir, compass, windSpeed, windAngle),
            (straightCourse, trueWindDir, leewayAngle),
            (0,), # tracking state
            (0,), # courseOffset
        )

    def checkCommand(self, posX, posY):
        """Execute commands from commandList."""
        # TODO make prettier
        while len(self.commandList) > 0:
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
                break

    def setDestination(self, destX, destY):
        """Set Sailor's destination to speecific coordinates."""
        self.destX = destX
        self.destY = destY

    def addFrame(self, *args):
        """Add Frame to FrameList. Method is called from run."""
        self.frameList.addFrame(
            len(self.frameList),
            (self.boatDirection, self.rudderAngle, self.mainSailAngle),
            (self.destX, self.destY, self.commandListIndex),
            *args,
        )


def trueWindDirection(gpsSpeed, gpsDir, windSpeed, windAngle):
    """Calculate trueWindDirection from gps and wind measurement."""
    (gpsX, gpsY) = polarToCart(gpsSpeed, gpsDir)
    (windX, windY) = polarToCart(windSpeed, windAngle)
    return cartToArg(gpsX + windX, gpsY + windY)
