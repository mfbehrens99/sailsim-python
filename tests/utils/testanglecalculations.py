import unittest
from math import pi

from sailsim.utils.anglecalculations import angleKeepInterval, directionKeepInterval


ALMOST_ANGLE_KEEP = 8
ALMOST_DIRECTION_KEEP = 8


class TestAngleCalculations(unittest.TestCase):
    """Test module `sailsim.utils.anglecalculations`."""

    def testAngleKeepInterval(self):
        self.assertAlmostEqual(angleKeepInterval( 0 + 0 * pi),  0, ALMOST_ANGLE_KEEP)
        self.assertAlmostEqual(angleKeepInterval( 0 + 2 * pi),  0, ALMOST_ANGLE_KEEP)
        self.assertAlmostEqual(angleKeepInterval( 0 - 2 * pi),  0, ALMOST_ANGLE_KEEP)
        self.assertAlmostEqual(angleKeepInterval( 1 + 0 * pi),  1, ALMOST_ANGLE_KEEP)
        self.assertAlmostEqual(angleKeepInterval( 1 + 2 * pi),  1, ALMOST_ANGLE_KEEP)
        self.assertAlmostEqual(angleKeepInterval( 1 - 2 * pi),  1, ALMOST_ANGLE_KEEP)
        self.assertAlmostEqual(angleKeepInterval(-1 + 0 * pi), -1, ALMOST_ANGLE_KEEP)
        self.assertAlmostEqual(angleKeepInterval(-1 + 2 * pi), -1, ALMOST_ANGLE_KEEP)
        self.assertAlmostEqual(angleKeepInterval(-1 - 2 * pi), -1, ALMOST_ANGLE_KEEP)

    def testDirectionKeepInterval(self):
        self.assertAlmostEqual(directionKeepInterval( 0 + 0 * pi),           0, ALMOST_DIRECTION_KEEP)
        self.assertAlmostEqual(directionKeepInterval( 0 + 2 * pi),           0, ALMOST_DIRECTION_KEEP)
        self.assertAlmostEqual(directionKeepInterval( 0 - 2 * pi),           0, ALMOST_DIRECTION_KEEP)
        self.assertAlmostEqual(directionKeepInterval( 1 + 0 * pi),           1, ALMOST_DIRECTION_KEEP)
        self.assertAlmostEqual(directionKeepInterval( 1 + 2 * pi),           1, ALMOST_DIRECTION_KEEP)
        self.assertAlmostEqual(directionKeepInterval( 1 - 2 * pi),           1, ALMOST_DIRECTION_KEEP)
        self.assertAlmostEqual(directionKeepInterval( 3 + 0 * pi),           3, ALMOST_DIRECTION_KEEP)
        self.assertAlmostEqual(directionKeepInterval( 3 + 2 * pi),           3, ALMOST_DIRECTION_KEEP)
        self.assertAlmostEqual(directionKeepInterval( 3 - 2 * pi),           3, ALMOST_DIRECTION_KEEP)
        self.assertAlmostEqual(directionKeepInterval(-1 + 0 * pi), -1 + 2 * pi, ALMOST_DIRECTION_KEEP)


if __name__ == '__main__':
    unittest.main()
