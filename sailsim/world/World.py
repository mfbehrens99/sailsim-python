class World:
    """Hold all objects that descripe the circumstances of the simulation."""

    def __init__(self, boat, wind, waterarea):
        self.boat = boat
        self.wind = wind
        self.waterarea = waterarea


    def __repr__(self):
        return "%s\n\n%s" % (self.boat, self.wind)
