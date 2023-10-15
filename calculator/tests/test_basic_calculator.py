"""
Contains unit tests for the calculator functions.
"""

import unittest
from calculator.basic_calculator import BasicCalculator


class TestCalculator(unittest.TestCase):
    """
    Unit tests for the BasicCalculator class.
    """

    def setUp(self):
        """
        Set up the calculator instance for testing.
        """
        self.calculator = BasicCalculator()

    def test_addition(self):
        """
        Test addition functionality of the BasicCalculator class.
        """
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtraction(self):
        """
        Test subtraction functionality of the BasicCalculator class.
        """
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        """
        Test multiplication functionality of the BasicCalculator class.
        """
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_division(self):
        """
        Test division functionality of the BasicCalculator class.
        """
        result = self.calculator.divide(6, 2)
        self.assertEqual(result, 3.0)

    def test_division_by_zero(self):
        """
        Test division by zero functionality of the BasicCalculator class.
        """
        result = self.calculator.divide(6, 0)
        self.assertEqual(result, "Cannot divide by zero")

    def test_invalid_input(self):
        """
        Test the handling of invalid input by the BasicCalculator class.
        """
        with self.assertRaises(TypeError):
            self.calculator.add(2, "3")
            self.calculator.subtract(2, "1")
            self.calculator.multiply(1, "")
            self.calculator.divide(10, "3")


if __name__ == "__main__":
    unittest.main()
