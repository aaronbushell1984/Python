
FILE = 'q5'
FUNCTION = 'name_from_email'

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
    from q5 import name_from_email as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, email, expected, result):
        message = FUNCTION+'('+email+')'
        message = message+'\n\nFull name extracted from '+email+' is '+expected+' - You returned '+result
        if not isinstance(result, str):
            message = message+'\n\nReturned value must be a string'
        return message

    def test_empty_returns_invalid_email(self):
        email = ''
        expected = 'Invalid email'
        result = test_function(email)
        message = self.explanation(email, expected, result)
        self.assertEqual(expected, result, msg=message)


    def test_missing_at_sign_returns_invalid_email(self):
        email = 'first.last.gmail.com'
        expected = 'Invalid email'
        result = test_function(email)
        message = self.explanation(email, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_missing_dot_returns_invalid_email(self):
        email = 'FirstLast@gmailcom'
        expected = 'Invalid email'
        result = test_function(email)
        message = self.explanation(email, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_valid_email_no_numbers_returns_full_name(self):
        email = 'john.smith@fdmgroup.com'
        expected = 'John Smith'
        result = test_function(email)
        message = self.explanation(email, expected, result)
        self.assertEqual(expected, result, msg=message)
        
    def test_valid_email_with_numbers_returns_full_name(self):
        email = 'john.smith123@fdmgroup.com'
        expected = 'John Smith'
        result = test_function(email)
        message = self.explanation(email, expected, result)
        self.assertEqual(expected, result, msg=message)

if __name__ == '__main__':
    unittest.main()