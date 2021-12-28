from copy import deepcopy

from sailsim.boat import Boat
from sailsim.wind import Wind


class Simulation:
    """Main simulation class in this project."""

    def __init__(self, boat: Boat, wind: Wind, timestep: float, lastFrame: int=None):
        """
        Create Simulation.

        Args:
            boat:       boat object to simulate
            wind:       wind of the simulation
            timestep:   time difference between frames
            lastFrame:  number of frames to be simulated, default: no end
        """
        self.boat: Boat = boat
        self.wind: Wind = wind
        self.initBoat: Boat = deepcopy(boat)

        # Timing
        self.timestep: float = timestep
        self.frame: int = 0
        self.lastFrame: int = lastFrame

    def run(self, steps: int=0) -> None:
        """Run whole Simulation if lastFrame is set."""
        if steps < 1:
            # Check if lastFrame exisists
            if self.lastFrame is None:
                raise Exception('Simulation has no lastFrame')
            while self.frame <= self.lastFrame:
                self.step()
        else:
            for i in range(steps):
                self.step()

    def step(self) -> None:
        """Run one step of the Simulation."""
        # Preperations
        time: float = self.frame * self.timestep

        # Calculate Forces on boat
        (boatX, boatY) = self.boat.getPos()                           # Fetch boat position
        (windX, windY) = self.wind.getWindCart(boatX, boatY, time)    # Get wind
        (forceX, forceY, torque) = self.boat.resultingCauses(windX, windY)

        # Save frame
        self.boat.frameList.grabFrame(self, self.boat)
        self.frame += 1

        self.boat.runSailor()

        # Move Boat
        self.boat.applyCauses(forceX, forceY, torque, self.timestep)
        self.boat.moveInterval(self.timestep)


    def getTime(self) -> float:
        """Return the elapsed time since the start of the simulation."""
        return self.timestep * self.frame

    def totalTime(self) -> float:
        """Return the total time that will elapse throughout the simulation."""
        return self.timestep * self.lastFrame


    def reset(self) -> None:
        """Set simulation to the first frame recorded."""
        # Reset Boat
        self.boat = deepcopy(self.initBoat)

        # Reset Simulation
        self.boat.frameList.reset()
        self.frame = 0


    def __repr__(self) -> str:
        """Return basic information about the simulation."""
        if self.lastFrame is None:
            return "sailsim @frm%s(%ss), %sms\n%s\n----------" % (self.frame, self.getTime(), self.timestep * 1000, self.boat, self.wind)
        return "sailsim @frm%s/%s(%ss,%s%%), %sms\n%s\n----------" % (self.frame, self.lastFrame, self.getTime(), str(round(self.frame * 100 / self.lastFrame, 1)).zfill(4), self.timestep * 1000, self.boat, self.wind)

    def __len__(self) -> int:
        """Return number of frames. Might be None."""
        return self.lastFrame
