from copy import deepcopy
from math import ceil, log2

from sailsim.utils.coordconversion import cartToRadius

from sailsim.simulation.FrameList import FrameList


class Simulation:
    """Main simulation class in this project."""

    def __init__(self, world, timestep, lastFrame=None):
        """
        Create Simulation.

        Args:
            world:      world object that contains all information about the world to simulate
            timestep:   time difference between frames
            lastFrame:  number of frames to be simulated, default: no end
        """
        self.world = world
        self.initWorld = deepcopy(world)
        self.frameList = FrameList()

        # Timing
        self.timestep = timestep
        self.frame = 0
        self.subframe = 0
        self.lastFrame = lastFrame

    def run(self):
        """Run whole Simulation if lastFrame is set."""
        # Check if lastFrame exisists
        if self.lastFrame is None:
            raise Exception('Simulation has no lastFrame')
        while self.frame <= self.lastFrame:
            self.step()

    def step(self):
        """Run one step of the Simulation."""
        # Preperations
        time = self.frame * self.timestep

        # Calculate Forces on boat
        (boatX, boatY) = self.world.boat.getPos()                           # Fetch boat position
        (windX, windY) = self.world.wind.getWindCart(boatX, boatY, time)    # Get wind
        (forceX, forceY) = self.world.boat.resultingForce(windX, windY)     # Get resulting Force

        # Subframing
        oldSubFrame = self.subframe                         # Save old subframe
        subframeThreshold = 2 ** 4                          # 1 / maxValue until new substep
        deltav = cartToRadius(forceX, forceY) * self.timestep / self.world.boat.mass # calculate change of speed of boat
        subframe = ceil(log2(deltav * subframeThreshold))   # calculate ideal subframe
        self.subframe = min(8, max(0, subframe))            # keep subframe in interval

        # Bring frame to integer values (get all binary decimal places to 0)
        if oldSubFrame > self.subframe:     # Only run this part when simulation wants to run on a lower subframe value
            while oldSubFrame > self.subframe and self.frame % 2**(-oldSubFrame + 1) == 0: # If ... and the oldSubFrame'th place in binary is 0
                oldSubFrame -= 1            # decrease subframe by one
            self.subframe = oldSubFrame     # Use calculated subframe as subframe

        subfrFactor = 1 / (2 ** self.subframe)
        # print(deltav, deltav * subfrFactor, subframe, self.subframe, sep="\t")

        # Save frame
        self.frameList.grabFrame(self)
        self.frame += 1 * subfrFactor

        # Move Boat
        self.world.boat.applyForce(forceX, forceY, self.timestep * subfrFactor)
        self.world.boat.moveInterval(self.timestep * subfrFactor)


    def getTime(self):
        """Return the elapsed time since the start of the simulation."""
        return self.timestep * self.frame

    def totalTime(self):
        """Return the total time that will elapse throughout the simulation."""
        return self.timestep * self.lastFrame


    def reset(self):
        """Set simulation to the first frame recorded."""
        # Reset Boat
        self.world = deepcopy(self.initWorld)

        # Reset Simulation
        self.frameList.reset()
        self.frame = 0


    def __repr__(self):
        """Return basic information about the simulation."""
        if self.lastFrame is None:
            return "sailsim @frm%s(%ss), %sms\n%s\n----------" % (self.frame, self.getTime(), self.timestep * 1000, self.world)
        return "sailsim @frm%s/%s(%ss,%s%%), %sms\n%s\n----------" % (self.frame, self.lastFrame, self.getTime(), str(round(self.frame * 100 / self.lastFrame, 1)).zfill(4), self.timestep * 1000, self.world)

    def __len__(self):
        """Return number of frames. Might be None."""
        return self.lastFrame
