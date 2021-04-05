class Frame():
    """This class is holding all data about one frame in the simulation."""

    def __init__(self):
        self.frameNr = self.time = None

        self.windTable = []

        self.boatPosX = self.boatPosY = None
        self.boatSpeedX = self.boatSpeedY = None
        self.boatDirection = None

        self.boatMainSailAngle = None
        self.boatRudderAngle = None

        self.boatApparentWindX = self.boatApparentWindY = None
        self.boatApparentWindAngle = None
        self.boatLeewayAngle = None
        self.boatAngleOfAttack = None

        self.boatForceX = self.boatForceY = None
        self.boatSailDragX = self.boatSailDragY = None
        self.boatSailLiftX = self.boatSailLiftY = None
        self.boatWaterDragX = self.boatWaterDragY = None
        self.boatWaterLiftX = self.boatWaterLiftY = None

        self.boatMomentum = None
        self.boatWaterDragMomentum = None
        self.boatRudderMomentum = None


    def collectSimulation(self, simulation):
        self.frameNr = simulation.frame
        self.time = simulation.getTime()

    def collectBoat(self, boat):
        """Collect and save all information about the boat."""
        self.boatPosX = boat.posX
        self.boatPosY = boat.posY
        self.boatSpeedX = boat.speedX
        self.boatSpeedY = boat.speedY
        self.boatDirection = boat.direction
        self.boatAngSpeed = boat.angSpeed

        self.boatMainSailAngle = boat.mainSailAngle
        # self.boatRudderAngle = boat.rudderAngle

        h = boat.dataHolder
        (self.boatApparentWindX, self.boatApparentWindY) = (h.apparentWindX, h.apparentWindY)
        self.boatApparentWindAngle = h.apparentWindAngle
        self.boatLeewayAngle = h.leewayAngle
        self.boatAngleOfAttack = h.angleOfAttack

        (self.boatForceX, self.boatForceY) = (h.forceX, h.forceY)
        (self.boatSailDragX, self.boatSailDragY) = (h.sailDragX, h.sailDragY)
        (self.boatSailLiftX, self.boatSailLiftY) = (h.sailLiftX, h.sailLiftY)
        (self.boatWaterDragX, self.boatWaterDragY) = (h.waterDragX, h.waterDragY)
        (self.boatWaterLiftX, self.boatWaterLiftY) = (h.waterLiftX, h.waterLiftY)

        self.boatMomentum = h.momentum
        self.boatWaterDragMomentum = h.waterDragMomentum
        self.boatRudderMomentum = h.rudderMomentum

    def collectWind(self, wind, x, y, size, distance):
        """Collect and save all information about the wind."""
        windTable = []
        for i in range(-size, size + 1):
            for j in range(-size, size + 1):
                coordX = x + i * distance
                coordY = y + j * distance
                windTable.append(wind.getWindCart(coordX, coordY, self.time))
        self.windTable = windTable

    def getWindList(self):
        windList = []
        for wind in self.windTable:
            windList.append(wind[0])
            windList.append(wind[1])
        return windList

    def getCSVLine(self):
        """Return string that contains all data about this frame."""
        data = [
            self.frameNr, self.time,
            self.boatPosX, self.boatPosY, self.boatSpeedX, self.boatSpeedY, self.boatDirection, self.boatAngSpeed,
            self.boatApparentWindX, self.boatApparentWindY, self.boatApparentWindAngle, self.boatLeewayAngle, self.boatAngleOfAttack,
            self.boatForceX, self.boatForceY,
            self.boatSailDragX, self.boatSailDragY, self.boatSailLiftX, self.boatSailLiftY,
            self.boatWaterDragX, self.boatWaterDragY, self.boatWaterLiftX, self.boatWaterLiftY,
            self.boatMomentum, self.boatWaterDragMomentum, self.boatRudderMomentum,
        ]
        data.extend(self.getWindList())
        dataStr = [f'{x:.4f}'.rstrip('0').rstrip('.') for x in data] # FIXME very slow and inflexible
        return ",".join(dataStr)
