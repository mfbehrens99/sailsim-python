import Boat
import Wind

class World:
    """Holds all objects that descripe the circumstances of the simulation"""

    def __init__(self, boat, wind, waterarea):
        self.boat = boat
        self.wind = wind
        self.waterarea = waterarea
