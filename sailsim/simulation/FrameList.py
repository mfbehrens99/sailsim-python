from sailsim.simulation.Frame import Frame


class FrameList():
    """Keep all Frames of a simulation and export the data."""

    def __init__(self):
        self.frames = []

        self.windSize = 0
        self.windDistance = 10

    def grabFrame(self, simulation, boat, wind):
        """Append new frame with all information to list."""
        time = simulation.getTime()
        (posX, posY) = (boat.posX, boat.posY) # TODO use method of boat class when implemented
        frame = Frame(time)
        frame.collectBoat(boat)
        frame.collectWind(wind, posX, posY, self.windSize, self.windDistance)
        self.frames.append(frame)


    def toCSV(self, name="output"):
        """Generate .csv file and write it to drive."""
        if not name.endswith(".csv"):
            name += ".csv"
        file = open(name, "w")

        output = self.getCSVHeader()
        for frame in self.frames:
            output += frame.toCSV()
        file.write(output)
        file.close()

    def getCSVHeader(self):
        """Generate head of .csv file."""
        return "\n"
