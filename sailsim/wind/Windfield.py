from sailsim.utils.coordconversion import cartToPolar


class Windfield:
    """Describe a partion of the wind."""

    def __init__(self, x, y):
        self.speedX = x
        self.speedY = y
        self.name = "Windfield"

    def getWindCart(self, x, y, t):
        """Return cartesian components of the windfield at the position (x, y) as a tuple."""
        return (self.speedX, self.speedY)

    def getWind(self, x, y, t):
        """Return direction and speed of the windfield at the position (x, y) as a tuple."""
        (cartX, cartY) = self.getWindCart(x, y, t)
        return cartToPolar(cartX, cartY)


    def setName(self, name):
        self.name = name
