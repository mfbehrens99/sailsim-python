class Simulation:
    """Main simulation class in this project"""

    def __init__(self, world, timestep, lastFrame=None):
        self.world = world

        # Timing
        self.timestep = timestep
        self.frame = 0
        self.lastFrame = lastFrame

    def run(self):
        """Run whole Simulation if lastFrame is set."""
        # Check if lastFrame exisists
        if self.lastFrame is None:
            raise Exception('Simulation has no lastFrame')
        while self.frame < self.lastFrame:
            self.step()

    def step(self):
        """Run one step of the Simulation."""

        # Preperations
        time = self.frame * self.timestep

        # Simulation starts
        (boatX, boatY) = (self.world.boat.posX, self.world.boat.posY)       # Fetch boat position
        (windX, windY) = self.world.wind.getWindCart(boatX, boatY, time)    # Get wind

        # Let wind interact with boat
        (forceX, forceY) = self.world.boat.resultingForce(windX, windY)
        self.world.boat.applyForce(forceX, forceY, self.timestep)
        self.world.boat.moveInterval(self.timestep)

        # TODO gather information for display

        self.frame += 1
