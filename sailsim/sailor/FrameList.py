"""This module contains the FrameList class."""

from csv import writer

from sailsim.simulation.Frame import Frame


class FrameList():
    """Keep all Frames of a simulation and export the data."""

    def __init__(self):
        self.frames = []

    def grabFrame(self, *args):
        """Append new frame with all information to list."""
        f = Frame(*args)
        self.frames.append(f)

    def reset(self):
        """Delete all previously saved frames."""
        self.frames = []

    def getCSVHeader(self):
        """Generate head of .csv file."""
        return [
            "frameNr",
            "boatDirection", "rudderAngle", "mainSailAngle",
            "destX", "destY", "commandListIndex",
            "posX", "posY", "gpsSpeed", "gpsDir", "compass", "windSpeed", "windAngle",
            "straightCourse", "trueWindDirection", "leewayAngle",
            "tackingState",
            "courseOffset",
        ]

    def saveCSV(self, name="sailor.csv"):
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
