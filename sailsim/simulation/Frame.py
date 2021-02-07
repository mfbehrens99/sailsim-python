class Frame():
    """This class is holding all data about one frame in the simulation."""

    def __init__(self, time):
        self.time = time
        self.windTable = []

    def collectBoat(self, boat):
        """Collect and save all information about the boat."""
        # TODO write collectBoat()

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

    def toCSVLine(self):
        # TODO write toCSVLine
        return "\n"
