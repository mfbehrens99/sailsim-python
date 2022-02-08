from math import pi

from sailsim.utils.coordconversion import cartToPolar


class Windfield:
    """Describe a partion of the wind."""

    def __init__(self, x, y):
        self.speedX = x
        self.speedY = y

    def getWindCart(self, _x=0, _y=0, _t=0):
        """Return cartesian components of the windfield at the position (x, y) as a tuple."""
        return (self.speedX, self.speedY)

    def getWind(self, _x=0, _y=0, _t=0):
        """Return direction and speed of the windfield at the position (x, y) as a tuple."""
        (cartX, cartY) = self.getWindCart()
        return cartToPolar(cartX, cartY)

    def __repr__(self):
        (speed, direction) = self.getWind()
        return f"Windfield: {speed}m/s @{direction * 180 / pi}"
