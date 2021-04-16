"""This module contains the FrameList class."""

from csv import writer

from sailsim.simulation.Frame import Frame


class FrameList():
    """Keep all Frames of a simulation and export the data."""

    def __init__(self):
        self.frames = []

    def grabFrame(self, simulation):
        """Append new frame with all information to list."""
        (posX, posY) = simulation.world.boat.getPos()
        frame = Frame()
        frame.collectSimulation(simulation)
        frame.collectBoat(simulation.world.boat)
        self.frames.append(frame)

    def reset(self):
        """Delete all previously saved frames."""
        self.frames = []

    def getCoordinateList(self):
        """Return a list of all coordinates saved in this frameList."""
        out = []
        for f in self.frames:
            out.append((f.boatPosX, f.boatPosY))
        return out

    def getCSVHeader(self):
        """Generate head of .csv file."""
        return [
            "frame", "time",
            "boatPosX", "boatPosY", "boatSpeedX", "boatSpeedY", "boatDirection",
            "boatMainSailAngle", "boatRudderAngle",
            "boatApparentWindX", "boatApparentWindY", "boatApparentWindAngle", "boatLeewayAngle", "boatAngleOfAttack",
            "boatForceX", "boatForceY",
            "boatSailDragX", "boatSailDragY", "boatSailLiftX", "boatSailLiftY",
            "boatWaterDragX", "boatWaterDragY", "boatWaterLiftX", "boatWaterLiftY",
            "boatWindX", "boatWindY",
        ]

    def saveCSV(self, name="output.csv"):
        """Generate .csv file and save it to drive."""
        if not name.endswith(".csv"):
            name += ".csv"
        with open(name, "w", newline="") as fs:
            csvWriter = writer(fs)
            csvWriter.writerow(self.getCSVHeader())
            for frame in self.frames:
                data = [f'{x:.4f}'.rstrip('0').rstrip('.') for x in frame.getData()]
                csvWriter.writerow(data)
            fs.close()

    def __len__(self):
        """Return length of the frameList."""
        return len(self.frames)
