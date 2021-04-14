from sailsim.simulation.Frame import Frame


class FrameList():
    """Keep all Frames of a simulation and export the data."""

    def __init__(self):
        self.frames = []

        self.windSize = 0
        self.windDistance = 10

    def grabFrame(self, simulation):
        """Append new frame with all information to list."""
        (posX, posY) = simulation.world.boat.getPos()
        frame = Frame()
        frame.collectSimulation(simulation)
        frame.collectBoat(simulation.world.boat)
        frame.collectWind(simulation.world.wind, posX, posY, self.windSize, self.windDistance)
        self.frames.append(frame)

    def reset(self):
        """Delete all previously saved frames."""
        self.frames = []

    def getCoordinateList(self):
        out = []
        for f in self.frames:
            out.append((f.boatPosX, f.boatPosY))
        return out

    def getCSV(self):
        """Generate .csv file and return it."""
        output = self.getCSVHeader() + "\n"
        for frame in self.frames:
            output += frame.getCSVLine() + "\n"
        return output

    def getCSVHeader(self):
        """Generate head of .csv file."""
        headers = [
            "frame", "time",
            "boatPosX", "boatPosY", "boatSpeedX", "boatSpeedY", "boatDirection",
            "boatMainSailAngle", "boatRudderAngle",
            "boatApparentWindX", "boatApparentWindY", "boatApparentWindAngle", "boatLeewayAngle", "boatAngleOfAttack",
            "boatForceX", "boatForceY",
            "boatSailDragX", "boatSailDragY", "boatSailLiftX", "boatSailLiftY",
            "boatWaterDragX", "boatWaterDragY", "boatWaterLiftX", "boatWaterLiftY",
        ]
        headers.extend(self.getWindHeader())
        return ",".join(headers)

    def getWindHeader(self):
        windHeader = []
        for i in range(0, 2 * self.windSize + 1):
            for j in range(0, 2 * self.windSize + 1):
                windHeader.append("wind" + str(i) + "_" + str(j) + "X")
                windHeader.append("wind" + str(i) + "_" + str(j) + "Y")
        return windHeader

    def saveCSV(self, name="output.csv"):
        """Generate .csv file and save it to drive."""
        if not name.endswith(".csv"):
            name += ".csv"
        file = open(name, "w")
        file.write(self.getCSV())
        file.close()

    def __len__(self):
        """Return length of the frameList."""
        return len(self.frames)
