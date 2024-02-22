""" module to test the SimpleMath class """
import unittest

class SimpleMath:
    """
    A class that provides basic mathematical operations.
    """

    @staticmethod
    def addition(a, b):
        """
        Adds two numbers and returns the result.

        Parameters:
        a (int): The first number.
        b (int): The second number.

        Returns:
        int: The sum of the two numbers.
        """
        return a + b

    @staticmethod
    def soustraction(a, b):
        """
        Subtracts two numbers and returns the result.

        Parameters:
        a (int): The first number.
        b (int): The second number.

        Returns:
        int: The difference between the two numbers.
        """
        return a - b

class TestSimpleMath(unittest.TestCase):
    """
    A class that provides test cases for the SimpleMath class.
    """
    def test_addition(self):
        """
        Tests the addition method of the SimpleMath class.
        """
        self.assertEqual(SimpleMath.addition(17, 12) , 29)

    def test_soustraction(self):
        """
        Tests the soustraction method of the SimpleMath class.
        """
        self.assertEqual(SimpleMath.soustraction(8, 2), (6))

if __name__== "__main__":
    unittest.main()
