class Simulation:
    """Main simulation class in this project"""

    interval = 1


    def __init__(self, interval, world, start=None, end=None):
        self.interval = interval

        self.world = world

        self.start = start
        self.end = end

    def run(self):
        """Runs Simulation"""
        #TODO write simulation

    def runStep(self):
        """Runs Simulation one step"""


    def __repr__(self):
        ret  = "sailsim (" + str(self.__class__) + ")\n"
        ret += "@" + str(self.frequence) + "Hz, frame " + str(self.frame) + "/" + str(self.maxFrames) + "\n"
        ret += self.world.__str__()
        return ret
