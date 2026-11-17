import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
         self.assertEqual(add(2, 3), 5)
         self.assertEqual(add(-1, 1), 0)
         self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)


    ######## Partner 1

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(-4, 3), -12)


    # def test_divide(self): # 3 assertions
    #     fill in code

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(4, 20), 5)
        self.assertEqual(divide(5, 15), 3)

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
         with self.assertRaises(ZeroDivisionError):
                 divide(0, 5)

    def test_logarithm(self): # 3 assertions
         self.assertEqual(logarithm(8, 2), 3)
         self.assertEqual(logarithm(9, 3), 2)
         self.assertEqual(logarithm(100, 10), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(8, 1)
    # ##########################
    
    ######## Partner 1

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)



    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(8, 15), 17)


    def test_sqrt(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(100), 10)
        with self.assertRaises(ValueError):
            square_root(-4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()