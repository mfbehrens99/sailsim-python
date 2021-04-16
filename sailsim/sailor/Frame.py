from csv import writer

class Frame:
    """Data frames for sailsim.sailor.sailor."""

    boatDirection = None
    rudderAngle = None
    mainSailAngle = None

    destX = destY = None
    commandListIndex = 0

    posX = posY = None
    gpsSpeed = None
    gpsDir = None
    compass = None
    windSpeed = None
    windAngle = None

    straightCourse = None
    trueWindDirection = None
    leewayAngle = None

    tackingState = None

    courseOffset = None

    def __init__(self, frameNr, results, commands, inputs, generalCalcs, rudderCalcs, sailCalcs):
        self.frameNr = frameNr
        self.setResults(results)
        self.setCommands(commands)
        self.setInputs(inputs)
        self.setGeneralCalcs(generalCalcs)
        self.setRudderCalcs(rudderCalcs)
        self.setSailCalcs(sailCalcs)

    def setResults(self, results):
        self.boatDirection, self.rudderAngle, self.mainSailAngle = results

    def setCommands(self, commands):
        self.destX, self.destY, self.commandListIndex = commands

    def setInputs(self, inputs):
        self.posX, self.posY, self.gpsSpeed, self.gpsDir, self.compass, self.windSpeed, self.windAngle = inputs

    def setGeneralCalcs(self, generalCalcs):
        self.straightCourse, self.trueWindDirection, self.leewayAngle = generalCalcs

    def setRudderCalcs(self, rudderCalcs):
        self.tackingState, = rudderCalcs

    def setSailCalcs(self, sailCalcs):
        self.courseOffset, = sailCalcs

    def getData(self):
        return [
            self.frameNr,
            self.boatDirection, self.rudderAngle, self.mainSailAngle,
            self.destX, self.destY, self.commandListIndex,
            self.posX, self.posY, self.gpsSpeed, self.gpsDir, self.compass, self.windSpeed, self.windAngle,
            self.straightCourse, self.trueWindDirection, self.leewayAngle,
            self.tackingState,
            self.courseOffset,
        ]
