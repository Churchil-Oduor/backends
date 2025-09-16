import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(calc.subtract(2, 5), -3)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(calc.divide(2, 1), 2)
        self.assertRaises(ValueError, calc.divide, 10, 3)


if __name__ == '__main__':
     unittest.main()
