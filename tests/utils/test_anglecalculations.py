"""Test module sailsim.utils.anglecalculations."""

from pytest import approx
from math import pi

from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval


def testAngleKeepInterval():
    assert angleKeepInterval( 0 + 0 * pi) == approx( 0)
    assert angleKeepInterval( 0 + 2 * pi) == approx( 0)
    assert angleKeepInterval( 0 - 2 * pi) == approx( 0)
    assert angleKeepInterval( 1 + 0 * pi) == approx( 1)
    assert angleKeepInterval( 1 + 2 * pi) == approx( 1)
    assert angleKeepInterval( 1 - 2 * pi) == approx( 1)
    assert angleKeepInterval(-1 + 0 * pi) == approx(-1)
    assert angleKeepInterval(-1 + 2 * pi) == approx(-1)
    assert angleKeepInterval(-1 - 2 * pi) == approx(-1)


def testDirectionKeepInterval():
    assert directionKeepInterval( 0 + 0 * pi) == approx(0)
    assert directionKeepInterval( 0 + 2 * pi) == approx(0)
    assert directionKeepInterval( 0 - 2 * pi) == approx(0)
    assert directionKeepInterval( 1 + 0 * pi) == approx(1)
    assert directionKeepInterval( 1 + 2 * pi) == approx(1)
    assert directionKeepInterval( 1 - 2 * pi) == approx(1)
    assert directionKeepInterval( 3 + 0 * pi) == approx(3)
    assert directionKeepInterval( 3 + 2 * pi) == approx(3)
    assert directionKeepInterval( 3 - 2 * pi) == approx(3)
    assert directionKeepInterval(-1 + 0 * pi) == approx(-1 + 2 * pi)
