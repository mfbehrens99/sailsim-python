class Frame():
    """This class is holding all data about one frame in the simulation."""

    def __init__(self, time):
        self.time = time
        self.windTable = []

        self.boatPosX = None
        self.boatPosY = None
        self.boatSpeedX = None
        self.boatSpeedY = None

    def collectBoat(self, boat):
        """Collect and save all information about the boat."""
        self.boatPosX = boat.posX
        self.boatPosY = boat.posY
        self.boatSpeedX = boat.speedX
        self.boatSpeedY = boat.speedY

    def collectWind(self, wind, x, y, size, distance):
        """Collect and save all information about the wind."""
        self.windTable = []
        for i in range(-size, size + 1):
            row = []
            for j in range(-size, size + 1):
                coordX = x + i * distance
                coordY = y + j * distance
                row.append(wind.getWindCart(coordX, coordY, self.time))
            self.windTable.append(row)

    def getCSVLine(self):
        """Return string that contains all data about this frame."""
        # TODO write toCSVLine
        return "%s,%f,%f,%f,%f\n" % (self.time, self.boatPosX, self.boatPosY, self.boatSpeedX, self.boatSpeedY)
