class Simulation:
    """Main simulation class in this project"""

    def __init__(self, world, timestep, lastFrame=None):
        self.world = world

        # Timing
        self.timestep = timestep
        self.frame = 0
        self.lastFrame = lastFrame

    def run(self):
        """Runs Simulation"""
        if self.lastFrame is None:
            raise Exception('Simulation has no lastFrame')
        while self.frame < self.lastFrame:
            self.step()

    def step(self):
        """Runs Simulation one step"""

        # Preperations
        time = self.frame * self.timestep

        # Simulation starts
        # Fetch boat position
        (boatX, boatY) = (self.world.boat.posX, self.world.boat.posY)

        # Get wind
        (windX, windY) = self.world.wind.getWindCart(boatX, boatY, time)

        # Let wind interact with boat
        (forceX, forceY) = self.world.boat.resultingForce(windX, windY) # TODO it is probaply better to not pass the force back to the simulation
        self.world.boat.applyForce(forceX, forceY, self.timestep)
        self.world.boat.moveInterval(self.timestep)

        #TODO gather information for display

        self.frame += 1
