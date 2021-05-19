
FILE = 'q2'
FUNCTION = 'cat_age'

import os
import sys
import unittest

# Do not show the Traceback error
__unittest = True

# See if the user has put their code in the correct file name
print('----------------------------------------------------------------------')
if not os.path.isfile(FILE+'.py'):
    print('The file "'+FILE+'.py" does not exist')
    print('\nFAILED (errors=1)')
    sys.exit(2)

# See if they use the correct function name
f = open(FILE+'.py', 'r')
text = f.read().replace(' ', '')
f.close()
if 'def'+FUNCTION+'(' not in text:
    print('The function "'+FUNCTION+'" does not exist in file: '+FILE+'.py')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(3)

# If the function exists but does not import then there are syntax errors
try:
    from q2 import cat_age as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, input_age, expected, result):
        message = FUNCTION+'('+str(input_age)+')'
        message = message+'\n\nCat age in human years: '+str(input_age)
        message = message+'\nExpected result: '+str(expected)
        message = message+'\nYou returned: '+str(result)
        if not isinstance(result, int):
            message = message+'\n\nReturned value must be an integer'
        return message

    def test_minus_1(self):
        input_age = -1
        expected = 0
        result = test_function(input_age)
        message = self.explanation(input_age, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_0(self):
        input_age = 0
        expected = 0
        result = test_function(input_age)
        message = self.explanation(input_age, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_1(self):
        input_age = 1
        expected = 15
        result = test_function(input_age)
        message = self.explanation(input_age, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_2(self):
        input_age = 2
        expected = 24
        result = test_function(input_age)
        message = self.explanation(input_age, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_3(self):
        input_age = 3
        expected = 28
        result = test_function(input_age)
        message = self.explanation(input_age, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_5(self):
        input_age = 5
        expected = 36
        result = test_function(input_age)
        message = self.explanation(input_age, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_8(self):
        input_age = 8
        expected = 48
        result = test_function(input_age)
        message = self.explanation(input_age, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_10(self):
        input_age = 10
        expected = 56
        result = test_function(input_age)
        message = self.explanation(input_age, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_15(self):
        input_age = 15
        expected = 76
        result = test_function(input_age)
        message = self.explanation(input_age, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_20(self):
        input_age = 20
        expected = 96
        result = test_function(input_age)
        message = self.explanation(input_age, expected, result)
        self.assertEqual(expected, result, msg=message)


if __name__ == '__main__':
    unittest.main()
