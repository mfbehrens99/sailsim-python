from math import sqrt


class Waypoint:
    """Holds information about waypoints of the boat."""

    def __init__(self, destX, destY, radius):
        self.destX = destX
        self.destY = destY
        self.radius = radius

        self.programmed = False

    def checkWaypoint(self, sailor, posX, posY):
        """Check if the destination is already reached and set destination once."""
        if sqrt(pow(self.destX - posX, 2) + pow(self.destY - posY, 2)) <= self.radius:
            self.programmed = False
            return True
        else:
            if not self.programmed:
                sailor.setDestination(self.destX, self.destY)
            return False


# TODO write other commands
# class Command:
#     """Holds information about actions of the boat."""
#     def __init__(self):
#         pass
#
#     def checkCommand():
#         return True


commandListExample = [Waypoint(10, -20, 1), Waypoint(-10, -10, 1), Waypoint(-30, 30, 1), Waypoint(20, 20, 1), Waypoint(10, -5, 1), Waypoint(100, 0, 1)]
