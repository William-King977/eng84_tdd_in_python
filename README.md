# Test Driven Development (TDD)
### Why should we use TDD?
### What are te benefits of using TDD?

### Best use cases
 * We will use Pytest unit test in Python to implement TDD
 * TDD is widely used and is the cheapest way to test the 
   code or implement test driven development.
   
### Best Practices
 * Write the smallest possible test case that matches what 
   we need to program
   
 * Following the TDD cycle:
   * TDD cycle starts with everything failing 
   * Write the code to pass the test     
   * Refactor the code for the next test 
   * This continues until all the tests have successfully 
      passed
 * Naming conventions are extremely important when it comes 
   to TDD in Python
 * Place tests and code in separate files

### Assert methods
Some assert methods available from the `TestCase` class:

|Method                    | Checks that         |New in|
|:---                      |:---                 |:---|
|assertEqual(a, b)         |a == b               ||
|assertNotEqual(a, b)      |a != b               ||  
|assertTrue(x)             |bool(x) is True      ||  
|assertFalse(x)            |bool(x) is False     ||  
|assertIs(a, b)            |a is b               |3.1|
|assertIsNot(a, b)         |a is not b           |3.1|
|assertIsNone(x)           |x is None            |3.1|
|assertIsNotNone(x)        |x is not None        |3.1|
|assertIn(a, b)            |a in b               |3.1|
|assertNotIn(a, b)         |a not in b           |3.1|
|assertIsInstance(a, b)    |isinstance(a, b)     |3.2|
|assertNotIsInstance(a, b) |not isinstance(a, b) |3.2|

### Example unit tests
Here are some unit tests. The file is named 
`test_unittest_simplecalc.py`.

```python
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
```

**Write the code to pass the tests.** This is the 
`simple_calc.py` file. Use `python -m pytest` in 
`test_unittest_simplecalc.py` to run the tests.
```python
class SimpleCalc():

    # Adds two numbers
    def add(self, value1, value2):
        return value1 + value2

    # Subtracts two numbers
    def subtract(self, value1, value2):
        return value1 - value2

    # Multiplies two numbers
    def multiply(self, value1, value2):
        return value1 * value2

    # Divides two numbers
    def divide(self, value1, value2):
        return value1 / value2
```

Running the tests with `python -m unittest discover -v` will
output:
```
test_add (test_unittest_simplecalc.CalcTest) ... ok
test_divide (test_unittest_simplecalc.CalcTest) ... ok
test_multiply (test_unittest_simplecalc.CalcTest) ... ok
test_subtract (test_unittest_simplecalc.CalcTest) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.004s

OK
```









