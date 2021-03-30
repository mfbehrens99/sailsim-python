from math import pi, sqrt

from sailsim.utils.coordconversion import polarToCart, cartToArg
from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval

from sailsim.sailor.Commands import *


class Sailor:
    """Calculate mainSailAngle and mainRudderAngle."""

    from .sailorgetset import setCommandList, configBoat, configSailor, importBoat

    destX = 0
    destY = 0

    rudderAngle = None
    boatDirection = None

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

        self.commandList = commandList

        self.tackingAngleBufferSize = 10 / 180 * pi

        self.straightCourse = 0
        self.trueWindDir = 0


    def run(self, posX, posY, gpsSpeed, gpsDir, compass, windSpeed, windDir):
        """Execute Sailor calculations and save resultes in object properties."""
        self.checkCommand(posX, posY)

        straightCourse = cartToArg(self.destX - posX, self.destY - posY)
        trueWindDir = trueWindDirection(gpsSpeed, gpsDir, windSpeed, directionKeepInterval(windDir + compass))
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
            pass
        else:
            # print("Straight")
            self.boatDirection = straightCourse - (leewayAngle if abs(leewayAngle) < 0.5 else 0) # TODO improve leeway calculations

        #   compensate leewayAngle

        # else tacking
        #   maybe compensate leeway

        # moaaaaar ...


        self.mainSailAngle = angleKeepInterval(-windDir * 1 / 2 + pi) # NOTE calculate mainSailAngle

        # print(round(straightCourse / pi * 180, 4), round(abs(angleKeepInterval(lln - straightCourse)) / pi * 180, 4), sep="\t")

    def checkCommand(self, posX, posY):
        # TODO make prettier
        while len(self.commandList) > 0:
            success = False
            if type(self.commandList[0]) == Waypoint:
                success = self.commandList[0].checkWaypoint(self, posX, posY)
            elif type(self.commandList[0]) == Command:
                pass # TODO run Command

            if success:
                del self.commandList[0]
            else:
                break

    def setDestination(self, destX, destY):
        self.destX = destX
        self.destY = destY

def trueWindDirection(gpsSpeed, gpsDir, windSpeed, windDir):
    """Calculate trueWindDirection from gps and wind measurement."""
    (gpsX, gpsY) = polarToCart(gpsSpeed, gpsDir)
    (windX, windY) = polarToCart(windSpeed, windDir)
    return cartToArg(gpsX + windX, gpsY + windY)
