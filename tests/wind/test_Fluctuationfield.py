"""Test sailsim.wind.Fluctuationfield.Fluctuationfield."""

from sailsim.wind.Fluctuationfield import Fluctuationfield


class TestWind:
    def setup(self):
        self.ff = Fluctuationfield()

    def test_getWindCart(self):
        self.ff.amplitude = 0
        assert self.ff.getWindCart(0, 0, 0) == (0, 0)
        assert self.ff.getWindCart(8, 2, 4) == (0, 0)

        (self.ff.speedX, self.ff.speedY) = (2, 7)
        assert self.ff.getWindCart(0, 0, 0) == (2, 7)
        assert self.ff.getWindCart(8, 2, 4) == (2, 7)
        # TODO think of more tests
