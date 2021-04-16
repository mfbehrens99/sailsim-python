"""This module contains the Frame class."""


class Frame():
    """This class is holding all data about one frame in the simulation."""

    frameNr = time = None

    boatWindX = boatWindY = None

    boatPosX = boatPosY = None
    boatSpeedX = boatSpeedY = None
    boatDirection = None

    boatMainSailAngle = None
    boatRudderAngle = None

    boatApparentWindX = boatApparentWindY = None
    boatApparentWindAngle = None
    boatLeewayAngle = None
    boatAngleOfAttack = None

    boatForceX = boatForceY = None
    boatSailDragX = boatSailDragY = None
    boatSailLiftX = boatSailLiftY = None
    boatWaterDragX = boatWaterDragY = None
    boatWaterLiftX = boatWaterLiftY = None

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
        self.boatApparentWindX, self.boatApparentWindY = h.apparentWindX, h.apparentWindY
        self.boatWindX, self.boatWindY = h.trueWindX, h.trueWindY
        self.boatApparentWindAngle = h.apparentWindAngle
        self.boatLeewayAngle = h.leewayAngle
        self.boatAngleOfAttack = h.angleOfAttack

        (self.boatForceX, self.boatForceY) = (h.forceX, h.forceY)
        (self.boatSailDragX, self.boatSailDragY) = (h.sailDragX, h.sailDragY)
        (self.boatSailLiftX, self.boatSailLiftY) = (h.sailLiftX, h.sailLiftY)
        (self.boatWaterDragX, self.boatWaterDragY) = (h.waterDragX, h.waterDragY)
        (self.boatWaterLiftX, self.boatWaterLiftY) = (h.waterLiftX, h.waterLiftY)

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
