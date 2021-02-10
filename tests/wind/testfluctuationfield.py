import unittest

from sailsim.wind.Fluctuationfield import Fluctuationfield


class TestWind(unittest.TestCase):
    def setUp(self):
        self.ff = Fluctuationfield()

    def testGetWindCart(self):
        self.ff.amplitude = 0
        self.assertEqual(self.ff.getWindCart(0, 0, 0), (0, 0))
        self.assertEqual(self.ff.getWindCart(8, 2, 0), (0, 0))
        self.assertEqual(self.ff.getWindCart(0, 0, 4), (0, 0))
        (self.ff.speedX, self.ff.speedY) = (2, 7)
        self.assertEqual(self.ff.getWindCart(0, 0, 0), (2, 7))
        self.assertEqual(self.ff.getWindCart(8, 2, 0), (2, 7))
        self.assertEqual(self.ff.getWindCart(0, 0, 4), (2, 7))
        # TODO think of more tests


if __name__ == '__main__':
    unittest.main()
