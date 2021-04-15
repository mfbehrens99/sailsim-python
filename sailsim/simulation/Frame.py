"""This module contains the Frame class."""


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

    def collectSimulation(self, simulation):
        """Collect and save information about the state of the simulation."""
        self.frameNr = simulation.frame
        self.time = simulation.getTime()

    def collectBoat(self, boat):
        """Collect and save all information about the boat."""
        self.boatPosX = boat.posX
        self.boatPosY = boat.posY
        self.boatSpeedX = boat.speedX
        self.boatSpeedY = boat.speedY
        self.boatDirection = boat.direction

        self.boatMainSailAngle = boat.mainSailAngle
        self.boatRudderAngle = boat.rudderAngle

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

    def collectWind(self, wind, x, y):
        """Collect and save all information about the wind."""
        self.boatWindX, self.boatWindY = wind.getWindCart(x, y, self.time)

    def getData(self):
        """Return string that contains all data about this frame."""
        return [
            self.frameNr, self.time,
            self.boatPosX, self.boatPosY, self.boatSpeedX, self.boatSpeedY, self.boatDirection,
            self.boatMainSailAngle, self.boatRudderAngle,
            self.boatApparentWindX, self.boatApparentWindY, self.boatApparentWindAngle, self.boatLeewayAngle, self.boatAngleOfAttack,
            self.boatForceX, self.boatForceY,
            self.boatSailDragX, self.boatSailDragY, self.boatSailLiftX, self.boatSailLiftY,
            self.boatWaterDragX, self.boatWaterDragY, self.boatWaterLiftX, self.boatWaterLiftY,
            self.boatWindX, self.boatWindY,
        ]
