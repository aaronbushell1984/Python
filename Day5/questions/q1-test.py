
FILE = 'q1'
FUNCTION = 'binary_odds'

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
    from q1 import binary_odds as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, input_string, expected, result):
        message = FUNCTION+'('+input_string+')'
        message = message+'\n\nBinary odd numbers in: '+input_string
        message = message+'\nExpected result: '+str(expected)
        message = message+'\nYou returned: '+str(result)
        if not isinstance(result, list):
            message = message+'\n\nReturned value must be a list'
        return message

    def test_1(self):
        input_string = '1'
        expected = ['1']
        result = test_function(input_string)
        message = self.explanation(input_string, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_10(self):
        input_string = '10'
        expected = []
        result = test_function(input_string)
        message = self.explanation(input_string, expected, result)
        self.assertEqual(expected, result, msg=message)
        
    def test_1_10(self):
        input_string = '1 10'
        expected = ['1']
        result = test_function(input_string)
        message = self.explanation(input_string, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_empty_string(self):
        input_string = ''
        expected = []
        result = test_function(input_string)
        message = self.explanation(input_string, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_1_101_100_1111(self):
        input_string = '1 101 100 1111'
        expected = ['1','101','1111']
        result = test_function(input_string)
        message = self.explanation(input_string, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_duplicates(self):
        input_string = '1 101 1 101 100'
        expected = ['1','101','1','101']
        result = test_function(input_string)
        message = self.explanation(input_string, expected, result)
        self.assertEqual(expected, result, msg=message)

if __name__ == '__main__':
    unittest.main()
