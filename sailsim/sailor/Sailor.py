from sailsim.utils.coordconversion import polarToCart, cartToArg


class Sailor:
    """Calculate mainSailAngle and mainRudderAngle"""

    from .sailorgetset import setCommandList, configBoat, configSailor, importBoat

    rudderAngle = None
    boatDirection = None

    mainSailAngle = None

    def __init__(self, boat=None):
        if boat is not None:
            self.importBoat(boat)

        self.commandList = []
        self.commandIndex = 0


    def run(self, posX, posY, gpsSpeed, gpsDir, compass, windSpeed, windDir):

        self.checkCommand()

        trueWindDir = trueWindDirection(gpsSpeed, gpsDir, windSpeed, windDir)

        # reachable in a straight line
        #   compensate leewayAngle

        # else tacking
        #   maybe compensate leeway

        # moaaaaar ...

        self.boatDirection = 0
        self.mainRudderAngle = 0

        self.mainSailAngle = 0 # TODO calculate mainSailAngle


    def checkCommand(self):
        """Run command or check if the active command has finished"""
        pass


def trueWindDirection(gpsSpeed, gpsDir, windSpeed, windDir):
    """Calculate trueWindDirection from gps and wind measurement."""
    (gpsX, gpsY) = polarToCart(gpsSpeed, gpsDir)
    (windX, windY) = polarToCart(windSpeed, windDir)
    return cartToArg(gpsX + windX, gpsY + windY)
