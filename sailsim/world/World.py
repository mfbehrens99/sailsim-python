class World:
    """Holds all objects that descripe the circumstances of the simulation"""

    def __init__(self, boat, wind, waterarea):
        self.boat = boat
        self.wind = wind
        self.waterarea = waterarea


    def __repr__(self):
        ret = str(self.boat) + "\n\n"
        ret += str(self.wind)
        return ret
