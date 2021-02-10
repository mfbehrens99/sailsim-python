class World:
    """Hold all objects that descripe the circumstances of the simulation."""

    def __init__(self, boat, wind, waterarea):
        """
        Create world.

        Args:
            boat:       boat object that hold all attributes and methods to simulate a boat
            wind:       wind object that hold all attributes and methods to simulate the wind
            waterArea:  borders of the water
        """
        self.boat = boat
        self.wind = wind
        self.waterarea = waterarea


    def __repr__(self):
        return str(self.boat)
