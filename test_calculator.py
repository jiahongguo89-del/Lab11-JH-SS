# https://github.com/jiahongguo89-del/Lab11-JH-SS
# Partner 1: Jiahong Guo
# Partner 2: Samuel Simoes

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    ######## Partner 2 ########

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)

    ######## Partner 1 ########

    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(5, 0), 0)
        self.assertEqual(mul(-4, 3), -12)

    def test_divide(self):
        self.assertAlmostEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(4, 20), 5)
        self.assertAlmostEqual(div(5, 15), 3)

    ######## Partner 2 ########

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(3, 9), 2)
        self.assertAlmostEqual(logarithm(10, 100), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 8)

    ######## Partner 1 ########

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(100), 10)

        with self.assertRaises(ValueError):
            square_root(-4)


if __name__ == "__main__":
    unittest.main()