"""This module includes everything to store the simulation of a boat."""

from numpy import ndarray

from sailsim.utils import Wrench


class Frame():
    """This class is holding all data about one frame in the simulation."""

    frameNr: int
    time: float

    windX: float
    windY: float
    pose: ndarray
    speed: ndarray

    boatMainSailAngle: float
    boatRudderAngle: float

    boatApparentWindX: float
    boatApparentWindY: float
    boatApparentWindAngle: float
    boatLeewayAngle: float
    boatAngleOfAttack: float

    wrench: Wrench
    wrenchSailDrag: Wrench
    wrenchSailLift: float
    wrenchCenterboardDrag: float
    wrenchCenterboardLift: float
    wrenchRudderDrag: float
    wrenchRudderLift: float
    wrenchHullDrag: float
    wrenchHullLift: float

    def collectSimulation(self, simulation) -> None:
        """Collect and save information about the state of the simulation."""
        self.frameNr = simulation.frame
        self.time = simulation.getTime()

    def collectBoat(self, boat) -> None:
        """Collect and save all information about the boat."""
        self.pose = boat.pose
        self.speed = boat.speed

        self.boatMainSailAngle = boat.mainSailAngle
        self.boatRudderAngle = boat.rudderAngle

        (self.boatApparentWindX, self.boatApparentWindY) = (boat.temp_apparentWindX, boat.temp_apparentWindY)
        self.boatApparentWindAngle = boat.temp_apparentWindAngle
        self.boatLeewayAngle = boat.temp_leewayAngle
        self.boatAngleOfAttack = boat.temp_angleOfAttack

        # temp_sailDrag: Wrench
        # temp_sailLift: Wrench
        # temp_centerboardDrag: Wrench
        # temp_centerboardLift: Wrench
        # temp_rudderDrag: Wrench
        # temp_rudderLift: Wrench
        # temp_hullDrag: Wrench

        self.wrench = boat.temp_wrench
        self.wrenchSailDrag = boat.temp_sailDrag
        self.wrenchSailLift = boat.temp_sailLift
        self.wrenchCenterboardDrag = boat.temp_centerboardDrag
        self.wrenchCenterboardLift = boat.temp_centerboardLift
        self.wrenchRudderDrag = boat.temp_rudderDrag
        self.wrenchRudderLift = boat.temp_rudderLift
        self.wrenchHullDrag = boat.temp_hullDrag

    def collectWind(self, wind, x, y) -> None:
        """Collect and save all information about the wind."""
        (self.windX, self.windY) = wind.getWindCart(x, y, self.time)

    def getCSVLine(self) -> str:
        """Return string that contains all data about this frame."""
        # FIXME does not work anymore
        # FIXME use csv module
        return "Pls fixme"
        # data = [
        #     self.frameNr, self.time,
        #     self.pose[0], self.pose[1], self.pose[2], self.speed[0], self.speed[1], self.speed[2],
        #     self.boatMainSailAngle, self.boatRudderAngle,
        #     self.boatApparentWindX, self.boatApparentWindY, self.boatApparentWindAngle, self.boatLeewayAngle, self.boatAngleOfAttack,
        #     self.boatForceX, self.boatForceY,
        #     self.boatSailDragX, self.boatSailDragY, self.boatSailLiftX, self.boatSailLiftY,
        #     self.boatCenterboardDragX, self.boatCenterboardDragY, self.boatCenterboardLiftX, self.boatCenterboardLiftY,
        #     self.boatRudderDragX, self.boatRudderDragY, self.boatRudderLiftX, self.boatRudderLiftY,
        #     self.boatTorque, self.boatWaterDragTorque, self.boatCenterboardTorque, self.boatRudderTorque,
        #     self.windX, self.windY,
        # ]
        # dataStr = [f'{x:.4f}'.rstrip('0').rstrip('.') for x in data]  # FIXME very slow and inflexible
        # return ",".join(dataStr)


class FrameList():
    """Keep all Frames of a boat and export the data."""

    def __init__(self) -> None:
        self.frames: list = []


    def grabFrame(self, simulation, boat) -> None:
        """Append new frame with all information to list."""
        (posX, posY) = boat.getPos()
        frame: Frame = Frame()
        frame.collectSimulation(simulation)
        frame.collectBoat(boat)
        frame.collectWind(simulation.wind, posX, posY)
        self.frames.append(frame)

    def reset(self) -> None:
        """Delete all previously saved frames."""
        self.frames = []

    def getCoordinateList(self) -> list[tuple[float, float]]:
        out = []
        for frame in self.frames:
            out.append((frame.pose[0], frame.pose[1]))
        return out

    def getCSV(self) -> str:
        """Generate .csv file and return it."""
        output = self.getCSVHeader() + "\n"
        for frame in self.frames:
            output += frame.getCSVLine() + "\n"
        return output

    def getCSVHeader(self) -> str:
        """Generate head of .csv file."""
        headers = [
            "frame", "time",
            "boatPosX", "boatPosY", "boatDirection", "boatSpeedX", "boatSpeedY", "boatAngSpeed",
            "boatMainSailAngle", "boatRudderAngle",
            "boatApparentWindX", "boatApparentWindY", "boatApparentWindAngle", "boatLeewayAngle", "boatAngleOfAttack",
            "boatForceX", "boatForceY",
            "boatSailDragX", "boatSailDragY", "boatSailLiftX", "boatSailLiftY",
            "boatWaterDragX", "boatWaterDragY", "boatWaterLiftX", "boatWaterLiftY",
            "boatRudderDragX", "boatRudderDragY", "boatRudderLiftX", "boatRudderLiftY",
            "boatTorque", "boatWaterDragTorque", "boatCenterboardTorque", "boatRudderTorque",
            "windX", "windY",
        ]
        return ",".join(headers)


    def saveCSV(self, name: str = "output.csv") -> None:
        """Generate .csv file and save it to drive."""
        if not name.endswith(".csv"):
            name += ".csv"
        with open(name, "w", encoding="utf-8") as file:
            file.write(self.getCSV())

    def __getitem__(self, key: int) -> Frame:
        return self.frames.__getitem__(key)

    def __setitem__(self, key: int, value) -> None:
        return self.frames.__setitem__(key, value)

    def __len__(self):
        """Return length of the frameList."""
        return len(self.frames)
