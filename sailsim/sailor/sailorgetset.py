def setCommandList(self, commandList, index=None):
    """Define command list and index if not set."""
    self.commandList = commandList

    if index is not None:
        self.commandIndex = index
    else:
        if self.commandIndex is None:
            self.commandIndex = 0


def configBoat(self):
    """Set important information about the boat."""
    pass


def configSailor(self):
    """Configure the way the sailor should work."""
    pass


def importBoat(self, boat):
    """Get data from a Boat object."""
    self.mass = boat.mass
    self.sailArea = boat.sailArea
    self.hullArea = boat.hullArea
    self.centerboardArea = boat.centerboardArea

    self.maxMainSailAngle = boat.maxMainSailAngle
    self.maxRudderAngle = boat.maxRudderAngle

    self.tackingAngleUpwind = boat.tackingAngleUpwind
    self.tackingAngleDownwind = boat.tackingAngleDownwind
