from copy import deepcopy

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
        (forceX, forceY) = self.world.boat.resultingForce(windX, windY)

        # Save frame
        self.frameList.grabFrame(self)
        self.frame += 1
        
        self.world.boat.runSailor()

        # Move Boat
        self.world.boat.applyForce(forceX, forceY, self.timestep)
        self.world.boat.moveInterval(self.timestep)


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
