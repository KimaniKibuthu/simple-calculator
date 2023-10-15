"""
Implements the Calculator class with arithmetic operations
"""

class BasicCalculator:
    """
    A simple calculator class for basic arithmetic operations.
    """

    def __init__(self):
        """
        Initialize the Calculator class.
        """
        pass

    def add(self, a, b):
        """
        Add two numbers.

        Args:
            a (int/float): First number.
            b (int/float): Second number.

        Returns:
            int/float: Result of the addition.
        """
        try:
            return a + b
        except TypeError:
            return "Invalid input. Both operands should be numbers."

    def subtract(self, a, b):
        """
        Subtract two numbers.

        Args:
            a (int/float): First number.
            b (int/float): Second number.

        Returns:
            int/float: Result of the subtraction.
        """
        try:
            return a - b
        except TypeError:
            return "Invalid input. Both operands should be numbers."

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Args:
            a (int/float): First number.
            b (int/float): Second number.

        Returns:
            int/float: Result of the multiplication.
        """
        try:
            return a * b
        except TypeError:
            return "Invalid input. Both operands should be numbers."

    def divide(self, a, b):
        """
        Divide two numbers.

        Args:
            a (int/float): Numerator.
            b (int/float): Denominator.

        Returns:
            int/float/str: Result of the division or error message if b is 0.
        """
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"
        except TypeError as e:
            raise e


if __name__ == "__main__":
    pass
