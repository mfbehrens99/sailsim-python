"""Test module sailsim.utils.coordconversion."""

from pytest import approx
from math import pi

from sailsim.utils.coordconversion import cartToRadius, cartToArg, polarToCart


def test_cartToRadius():
    assert cartToRadius( 0,  0) == 0
    assert cartToRadius( 1,  0) == 1
    assert cartToRadius( 0,  1) == 1
    assert cartToRadius(-1,  0) == 1
    assert cartToRadius( 0, -1) == 1
    assert cartToRadius( 3,  4) == 5
    assert cartToRadius(-3, -4) == 5


def test_cartToArg():
    assert cartToArg( 0,  1) == approx(0/4 * pi)
    assert cartToArg( 1,  1) == approx(1/4 * pi)
    assert cartToArg( 1,  0) == approx(2/4 * pi)
    assert cartToArg( 1, -1) == approx(3/4 * pi)
    assert cartToArg( 0, -1) == approx(4/4 * pi)
    assert cartToArg(-1, -1) == approx(5/4 * pi)
    assert cartToArg(-1,  0) == approx(6/4 * pi)
    assert cartToArg(-1,  1) == approx(7/4 * pi)


def test_polarToCart():
    assert polarToCart( 0,      0) == approx(( 0,  0))
    assert polarToCart( 0,      1) == approx(( 0,  0))
    assert polarToCart( 0,     pi) == approx(( 0,  0))
    assert polarToCart( 1, 0/2*pi) == approx(( 0,  1))
    assert polarToCart( 1, 1/2*pi) == approx(( 1,  0))
    assert polarToCart( 1, 2/2*pi) == approx(( 0, -1))
    assert polarToCart( 1, 3/2*pi) == approx((-1,  0))
    assert polarToCart( 2,      0) == approx(( 0,  2))
    assert polarToCart(-2,      0) == approx(( 0, -2))
    assert polarToCart( 2,     pi) == approx(( 0, -2))
    assert polarToCart(-2,     pi) == approx(( 0,  2))
