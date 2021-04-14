"""Test module sailsim.wind.Wind."""

from pytest import approx
from math import pi, sqrt

from sailsim.wind.Wind import Wind
from sailsim.wind.Windfield import Windfield


class TestWind():
    def setup(self):
        self.w = Wind([])

    def test_getWindCart(self):
        self.w.winds = []
        assert self.w.getWindCart(0, 0, 0) == (0, 0)

        self.w.winds = [Windfield(1, 0)]
        assert self.w.getWindCart(0, 0, 0) == (1, 0)

        self.w.winds = [Windfield(1, 0), Windfield(0, 1)]
        assert self.w.getWindCart(0, 0, 0) == (1, 1)

        self.w.winds = [Windfield(2, 1), Windfield(4, 1)]
        assert self.w.getWindCart(0, 0, 0) == (6, 2)

    def test_getWind(self):
        self.w.winds = [Windfield(1, 0)]
        assert self.w.getWind(0, 0, 0) == approx((1, pi / 2))

        self.w.winds = [Windfield(0, 1)]
        assert self.w.getWind(0, 0, 0) == approx((1, 0))

        self.w.winds = [Windfield(-1, 1)]
        assert self.w.getWind(0, 0, 0) == approx((sqrt(2), 7/4*pi))
