from math import pi

from sailsim.utils.coordconversion import cartToPolar


class Windfield:
    """Describe a partion of the wind."""

    def __init__(self, x: float, y: float) -> None:
        self.speedX: float = x
        self.speedY: float = y

    def getWindCart(self, _x: float = 0, _y: float = 0, _t: float = 0) -> tuple[float, float]:
        """Return cartesian components of the windfield at the position (x, y) as a tuple."""
        return (self.speedX, self.speedY)

    def getWind(self, _x: float = 0, _y: float = 0, _t: float = 0) -> tuple[float, float]:
        """Return direction and speed of the windfield at the position (x, y) as a tuple."""
        (cartX, cartY) = self.getWindCart()
        return cartToPolar(cartX, cartY)

    def __repr__(self) -> str:
        (speed, direction) = self.getWind()
        return f"Windfield: {speed}m/s @{direction * 180 / pi}"
