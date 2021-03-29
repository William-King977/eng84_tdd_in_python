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
 * TDD cycle starts with everything failing 
 * Write the code to pass the test
 * Refactor the code for the next test 
 * This continues until all the tests have successfully 
   passed
 * Naming conventions is extremely important when it comes 
   to TDD in Python
 * Place tests and code in separate files

Some assert methods:

|Method |   Checks that|   New in |
|:---                     |:---                    |:---|
|assertEqual(a, b)        |    a == b              ||
|assertNotEqual(a, b)     |    a != b              ||  
|assertTrue(x)            |    bool(x) is True     ||  
|assertFalse(x)           |    bool(x) is False    ||  
|assertIs(a, b)           |    a is b              |3.1|
|assertIsNot(a, b)        |    a is not b          |3.1|
|assertIsNone(x)          |    x is None           |3.1|
|assertIsNotNone(x)       |    x is not None       |3.1|
|assertIn(a, b)           |    a in b              |3.1|
|assertNotIn(a, b)        |    a not in b          |3.1|
|assertIsInstance(a, b)   |    isinstance(a, b)    |3.2|
|assertNotIsInstance(a, b)|    not isinstance(a, b)|3.2|









