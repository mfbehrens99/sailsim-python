from sailsim.simulation.Frame import Frame


class FrameList():
    """Keep all Frames of a simulation and export the data."""

    def __init__(self):
        self.frames = []

        self.windSize = 0
        self.windDistance = 10

    def grabFrame(self, simulation):
        """Append new frame with all information to list."""
        time = simulation.getTime()
        (posX, posY) = (simulation.world.boat.posX, simulation.world.boat.posY) # TODO use method of boat class when implemented
        frame = Frame(time)
        frame.collectBoat(simulation.world.boat)
        frame.collectWind(simulation.world.wind, posX, posY, self.windSize, self.windDistance)
        self.frames.append(frame)


    def getCSV(self):
        """Generate .csv file and write it to drive."""
        output = self.getCSVHeader()
        for frame in self.frames:
            output += frame.getCSVLine()
        return output

    def getCSVHeader(self):
        """Generate head of .csv file."""
        return "time,boatPosX,boatPosY,boatSpeedX,boatSpeedY\n"

    def saveCSV(self, name="output.csv"):
        if not name.endswith(".csv"):
            name += ".csv"
        file = open(name, "w")
        file.write(self.getCSV())
        file.close()
