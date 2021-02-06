import unittest
from math import pi

from sailsim.utils.coordconversion import cartToRadius, cartToArg, polarToCart


ALMOST_CART_TO_ARG = 8
ALMOST_POLAR_TO_CART = 8


class TestCoordConversion(unittest.TestCase):
    """Test module `sailsim.utils.coordconversion`."""

    def testCartToRadius(self):
        self.assertEqual(cartToRadius( 0,  0), 0)
        self.assertEqual(cartToRadius( 1,  0), 1)
        self.assertEqual(cartToRadius( 0,  1), 1)
        self.assertEqual(cartToRadius(-1,  0), 1)
        self.assertEqual(cartToRadius( 0, -1), 1)
        self.assertEqual(cartToRadius( 3,  4), 5)
        self.assertEqual(cartToRadius(-3, -4), 5)

    def testCartToArg(self):
        self.assertAlmostEqual(cartToArg( 0,  1), 0/4 * pi, ALMOST_CART_TO_ARG)
        self.assertAlmostEqual(cartToArg( 1,  1), 1/4 * pi, ALMOST_CART_TO_ARG)
        self.assertAlmostEqual(cartToArg( 1,  0), 2/4 * pi, ALMOST_CART_TO_ARG)
        self.assertAlmostEqual(cartToArg( 1, -1), 3/4 * pi, ALMOST_CART_TO_ARG)
        self.assertAlmostEqual(cartToArg( 0, -1), 4/4 * pi, ALMOST_CART_TO_ARG)
        self.assertAlmostEqual(cartToArg(-1, -1), 5/4 * pi, ALMOST_CART_TO_ARG)
        self.assertAlmostEqual(cartToArg(-1,  0), 6/4 * pi, ALMOST_CART_TO_ARG)
        self.assertAlmostEqual(cartToArg(-1,  1), 7/4 * pi, ALMOST_CART_TO_ARG)

    def testPolarToCart(self):
        self.assertAlmostEqual(polarToCart( 0,      0)[0],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 0,      0)[1],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 0,      1)[0],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 0,      1)[1],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 0,     pi)[0],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 0,     pi)[1],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 1, 0/2*pi)[0],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 1, 0/2*pi)[1],  1, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 1, 1/2*pi)[0],  1, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 1, 1/2*pi)[1],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 1, 2/2*pi)[0],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 1, 2/2*pi)[1], -1, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 1, 3/2*pi)[0], -1, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 1, 3/2*pi)[1],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 2,      0)[0],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 2,      0)[1],  2, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart(-2,      0)[0],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart(-2,      0)[1], -2, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 2,     pi)[0],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart( 2,     pi)[1], -2, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart(-2,     pi)[0],  0, ALMOST_POLAR_TO_CART)
        self.assertAlmostEqual(polarToCart(-2,     pi)[1],  2, ALMOST_POLAR_TO_CART)


if __name__ == '__main__':
    unittest.main()
