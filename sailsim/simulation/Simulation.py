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

    def runStep(self):
        """Runs Simulation one step"""
