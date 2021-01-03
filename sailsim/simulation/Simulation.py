class Simulation:
    """Main simulation class in this project"""

    interval = 1
    

    def __init__(self, interval, world, start=None, end=None):
        self.interval = interval

        self.word = world
        
        self.start = start
        self.end = end

    def run(self):
        pass

    def runStep(self):
        pass

