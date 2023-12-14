import unittest
from lab2 import Calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calc = Calculator()
        result = calc.calculate(5, '+', 3)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        calc = Calculator()
        result = calc.calculate(5, '-', 3)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        calc = Calculator()
        result = calc.calculate(5, '*', 3)
        self.assertEqual(result, 15)

    def test_division(self):
        calc = Calculator()
        result = calc.calculate(10, '/', 2)
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError) as context:
            calc.calculate(10, '/', 0)
        self.assertEqual(str(context.exception), "Error: Division by zero is not possible.")

if __name__ == "__main__":
    unittest.main()
