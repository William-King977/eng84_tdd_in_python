# Unit tests to check if the code runs without any errors
# pytest uses any file with the name including test*.py

# importing the file and class where we would write our code.
from simple_calc import SimpleCalc

# importing unittest to inherit TestCase to create our tests against the code
import unittest

class CalcTest(unittest.TestCase):

    calc = SimpleCalc() # Create SimpleCalc object

    # Using "test" in the same of our function will let
    # the python interpreter know that this needs to be tested
    def test_add(self):
        # Tests if 2 + 4 = 6. If true, the test will pass.
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        # Tests if 4 - 2 = 2. If true, the test will pass.
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        # Tests if 2 x 2 = 4. If true, the test will pass.
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_divide(self):
        # Tests if 15 / 3 = 5. If true, the test will pass.
        self.assertEqual(self.calc.divide(15, 3), 5)











