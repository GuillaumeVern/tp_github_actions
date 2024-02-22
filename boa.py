import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b
    
    @staticmethod
    def soustraction(a, b):
        return a - b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleMath.addition(17, 12) , 29)

    def test_soustraction(self):
        self.assertEqual(SimpleMath.soustraction(8, 2), (6))

if __name__== "__main__":
    unittest.main()