import math

class Windfield:
    """Describes a partion of the wind"""

    def __init__(self, speed, direction):
        self.speed = speed
        self.direction = direction

    def getWind(self, x, y):
        """Returns direction and speed of the windfield at the position (x,y) as a tuple"""
        return(self.speed,self.direction)

    def getWindCart(self, x, y):
        """Returns cartesian components of the windfield at the position (x,y) as a tuple"""
        (speed, direction) = self.getWind(x, y)
        x_cart = speed * math.cos(math.radians(direction))
        y_cart = speed * math.sin(math.radians(direction))
        return (x_cart,y_cart)
        #TODO slight errors due to rounding
