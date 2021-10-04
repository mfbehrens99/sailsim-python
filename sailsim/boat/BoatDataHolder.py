class BoatDataHolder():
    """Save temporary data for the Boat class."""
    def __init__(self):
        self.boatSpeed = None
        self.apparentWindSpeed = None

        self.apparentWindX = self.apparentWindY = None
        self.apparentWindAngle = None
        self.leewayAngle = None
        self.angleOfAttack = None

        self.forceX = self.forceY = None
        self.sailDragX = self.sailDragY = None
        self.sailLiftX = self.sailLiftY = None
        self.waterDragX = self.waterDragY = None
        self.waterLiftX = self.waterLiftY = None
        self.rudderDragX = self.rudderDragY = None
        self.rudderLiftX = self.rudderLiftY = None

        self.torque = None
        self.waterDragTorque = None
        self.rudderTorque = None
