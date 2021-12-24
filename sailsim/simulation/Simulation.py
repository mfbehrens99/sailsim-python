from copy import deepcopy


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

        # Timing
        self.timestep = timestep
        self.frame = 0
        self.lastFrame = lastFrame

    def run(self, steps=0):
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

    def step(self):
        """Run one step of the Simulation."""
        # Preperations
        time = self.frame * self.timestep

        # Calculate Forces on boat
        (boatX, boatY) = self.world.boat.getPos()                           # Fetch boat position
        (windX, windY) = self.world.wind.getWindCart(boatX, boatY, time)    # Get wind
        (forceX, forceY, torque) = self.world.boat.resultingCauses(windX, windY)

        # Save frame
        self.world.boat.frameList.grabFrame(self, self.world.boat)
        self.frame += 1

        self.world.boat.runSailor()

        # Move Boat
        self.world.boat.applyCauses(forceX, forceY, torque, self.timestep)
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
