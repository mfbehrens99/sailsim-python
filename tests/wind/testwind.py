import unittest
from math import pi, sqrt

from sailsim.wind.Wind import Wind
from sailsim.wind.Windfield import Windfield

ALMOST_GET_WIND = 8

class TestWind(unittest.TestCase):
    def setUp(self):
        self.w = Wind([])

    def testGetWindCart(self):
        self.w.winds = []
        self.assertEqual(self.w.getWindCart(0, 0, 0), (0, 0))
        self.w.winds = [Windfield(1,0)]
        self.assertEqual(self.w.getWindCart(0, 0, 0), (1, 0))
        self.w.winds = [Windfield(1,0), Windfield(0,1)]
        self.assertEqual(self.w.getWindCart(0, 0, 0), (1, 1))
        self.w.winds = [Windfield(2,1), Windfield(4,1)]
        self.assertEqual(self.w.getWindCart(0, 0, 0), (6, 2))

    def testGetWind(self):
        self.w.winds = [Windfield(1,0)]
        self.assertAlmostEqual(self.w.getWind(0, 0, 0)[0],       1, ALMOST_GET_WIND)
        self.assertAlmostEqual(self.w.getWind(0, 0, 0)[1],       0, ALMOST_GET_WIND)
        self.w.winds = [Windfield(0,1)]
        self.assertAlmostEqual(self.w.getWind(0, 0, 0)[0],       1, ALMOST_GET_WIND)
        self.assertAlmostEqual(self.w.getWind(0, 0, 0)[1],    pi/2, ALMOST_GET_WIND)
        self.w.winds = [Windfield(-1,1)]
        self.assertAlmostEqual(self.w.getWind(0, 0, 0)[0], sqrt(2), ALMOST_GET_WIND)
        self.assertAlmostEqual(self.w.getWind(0, 0, 0)[1],  5/4*pi, ALMOST_GET_WIND)

if __name__ == '__main__':
    unittest.main()
