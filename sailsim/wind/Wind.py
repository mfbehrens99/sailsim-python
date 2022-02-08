from typing import Union
from sailsim.utils.coordconversion import cartToPolar

from sailsim.wind.Windfield import Windfield
from sailsim.wind.Fluctuationfield import Fluctuationfield
from sailsim.wind.Squallfield import Squallfield


class Wind:
    """This class holds all windfields and calculates speed and direction of wind."""

    def __init__(self, winds: list[Union[Windfield, Fluctuationfield, Squallfield]]) -> None:
        self.winds = winds

    def getWindCart(self, x: float, y: float, t: float) -> tuple[float, float]:
        """Sum up and returns the speed and direction of all windfields."""
        sumX: float = 0
        sumY: float = 0
        for wind in self.winds:
            (windX, windY) = wind.getWindCart(x, y, t)
            sumX += windX
            sumY += windY
        return (sumX, sumY)

    def getWind(self, x: float, y: float, t: float) -> tuple[float, float]:
        """Return direction and speed of the windfield at the position (x,y) as a tuple."""
        (cartX, cartY) = self.getWindCart(x, y, t)
        return cartToPolar(cartX, cartY)

    def __repr__(self) -> str:
        # TODO make nicer
        windfields: int = sum(isinstance(x, Windfield) for x in self.winds)
        fluctuationfields: int = sum(type(x) is Fluctuationfield for x in self.winds)
        squallfields: int = sum(type(x) is Squallfield for x in self.winds)
        return f"Wind made up of {len(self.winds)} winds:\n\t{windfields} Windfields\n\t{fluctuationfields} Fluctuationfields\n\t{squallfields} Squallfields"

    def __len__(self) -> int:
        return len(self.winds)
