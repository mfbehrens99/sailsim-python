"""Test module sailsim.wind.Windfield."""

from pytest import approx
from math import pi, sqrt

from sailsim.wind.Windfield import Windfield


class TestWindfield():
    def test_getWindCart(self):
        w = Windfield(0, 0)
        assert w.getWindCart(0, 0, 0) == (0, 0)

        w = Windfield(1, 0)
        assert w.getWindCart(0, 0, 0) == (1, 0)

    def test_getWind(self):
        w = Windfield(1, 0)
        assert w.getWind(0, 0, 0) == approx((1, pi / 2))

        w = Windfield(0, 1)
        assert w.getWind(0, 0, 0) == approx((1, 0))

        w = Windfield(-1, 1)
        assert w.getWind(0, 0, 0) == approx((sqrt(2), 7/4*pi))
