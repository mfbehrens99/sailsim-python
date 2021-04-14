"""This module contains action slots for the SailsimGUI class."""


# Display for mapView
def actionViewShowWaypointLink(self, state):
    self.ui.mapView.displayWaypointLink = state
    self.ui.mapView.update()


def actionViewShowWaypoints(self, state):
    self.ui.mapView.displayWaypoints = state
    self.ui.mapView.update()


def actionViewShowMainSailMapView(self, state):
    self.ui.mapView.displayMainSail = state
    self.ui.mapView.update()


def actionViewShowRudderMapView(self, state):
    self.ui.mapView.displayRudder = state
    self.ui.mapView.update()


# Display for boatInspector
def actionViewShowBoat(self, state):
    self.ui.boatInspector.displayBoat = state
    self.ui.boatInspector.update()


def actionViewShowBoatDirection(self, state):
    self.ui.boatInspector.displayBoatDirection = state
    self.ui.boatInspector.update()


def actionViewShowSpeed(self, state):
    self.ui.boatInspector.displaySpeed = state
    self.ui.boatInspector.update()


def actionViewShowMainSailBoatInspector(self, state):
    self.ui.boatInspector.displayMainSail = state
    self.ui.boatInspector.update()


def actionViewShowRudderBoatInspector(self, state):
    self.ui.boatInspector.displayRudder = state
    self.ui.boatInspector.update()


def actionViewShowForces(self, state):
    self.ui.boatInspector.displayForces = state
    self.ui.boatInspector.update()
