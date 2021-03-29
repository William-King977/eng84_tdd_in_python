# Unit tests to check if the code runs without any errors

# importing the file and class where we would write our code.
from simple_calc import SimpleCalc

# importing unittest to inherit TestCase to create our tests against the code
import unittest

class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

    # Using "test" in the same of our function will let
    # the python interpreter know that this needs to be tested
    def test_add(self):
        # 2 + 2 = 4 outcome is true











