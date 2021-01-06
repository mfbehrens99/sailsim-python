from sailsim.utils.coordconversion import cartToPolar

class Windfield:
    """Describes a partion of the wind"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getWindCart(self, x, y, t):
        """Returns cartesian components of the windfield at the position (x,y) as a tuple"""
        return (self.x, self.y)

    def getWind(self, x, y, t):
        """Returns direction and speed of the windfield at the position (x,y) as a tuple"""
        (cartX, cartY) = self.getWindCart(x, y, t)
        return cartToPolar(cartX, cartY)
