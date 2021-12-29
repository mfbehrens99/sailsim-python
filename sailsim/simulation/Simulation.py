from copy import deepcopy


class Simulation:
    """Main simulation class in this project."""

    def __init__(self, boat, wind, timestep, lastFrame=None):
        """
        Create Simulation.

        Args:
            boat:       boat object to simulate
            wind:       wind of the simulation
            timestep:   time difference between frames
            lastFrame:  number of frames to be simulated, default: no end
        """
        self.boat = boat
        self.wind = wind
        self.initBoat = deepcopy(boat)

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
            for _ in range(steps):
                self.step()

    def step(self):
        """Run one step of the Simulation."""
        # Preperations
        time = self.frame * self.timestep

        # Calculate Forces on boat
        (boatX, boatY) = self.boat.getPos()                           # Fetch boat position
        (windX, windY) = self.wind.getWindCart(boatX, boatY, time)    # Get wind
        self.boat.updateTemporaryData(windX, windY)
        (forceX, forceY, torque) = self.boat.resultingCauses()

        # Save frame
        self.boat.frameList.grabFrame(self, self.boat)
        self.frame += 1

        self.boat.runSailor()

        # Move Boat
        self.boat.applyCauses(forceX, forceY, torque, self.timestep)
        self.boat.moveInterval(self.timestep)


    def getTime(self):
        """Return the elapsed time since the start of the simulation."""
        return self.timestep * self.frame

    def totalTime(self):
        """Return the total time that will elapse throughout the simulation."""
        return self.timestep * self.lastFrame


    def reset(self):
        """Set simulation to the first frame recorded."""
        # Reset Boat
        self.boat = deepcopy(self.initBoat)

        # Reset Simulation
        self.boat.frameList.reset()
        self.frame = 0


    def __repr__(self):
        """Return basic information about the simulation."""
        if self.lastFrame is None:
            return f"sailsim @frm{self.frame}({self.getTime()}s), {self.timestep * 1000}ms"
        return f"sailsim @frm{self.frame}/{self.lastFrame}({self.getTime()}s), {self.timestep * 1000}ms"

    def __len__(self):
        """Return number of frames. Might be None."""
        return self.lastFrame
