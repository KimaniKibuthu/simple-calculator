class Calculator:
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
        return a + b

    def subtract(self, a, b):
        """
        Subtract two numbers.

        Args:
            a (int/float): First number.
            b (int/float): Second number.

        Returns:
            int/float: Result of the subtraction.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Args:
            a (int/float): First number.
            b (int/float): Second number.

        Returns:
            int/float: Result of the multiplication.
        """
        return a * b

    def divide(self, a, b):
        """
        Divide two numbers.

        Args:
            a (int/float): Numerator.
            b (int/float): Denominator.

        Returns:
            int/float/str: Result of the division or error message if b is 0.
        """
        if b == 0:
            return 'Cannot divide by zero'
        else:
            return a / b

if __name__ == "__main__":
    pass
