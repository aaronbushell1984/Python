
FILE = 'q3'
FUNCTION = 'sumproduct'

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
    from q3 import sumproduct as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, list1, list2, expected, result):
        message = FUNCTION+'('+str(list1).replace(' ','')+','+str(list2).replace(' ','')+')'
        message = message+'\n\nThe sumproduct of '+str(list1).replace(' ','')+','+str(list2).replace(' ','')+' is '+str(expected)+'\n - You returned '+str(result)
        if not isinstance(result, int) and not isinstance(result, float):
            message = message+'\n\nReturned value must be an integer or a float'
        return message

    def test_empty_returns_0(self):
        list1 = []
        list2 = []
        expected = 0
        result = test_function(list1, list2)
        message = self.explanation(list1, list2, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_different_sizes_returns_0(self):
        list1 = [1]
        list2 = [1,2]
        expected = 0
        result = test_function(list1, list2)
        message = self.explanation(list1, list2, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_1_2_and_3_4_returns_11(self):
        list1 = [1,2]
        list2 = [3,4]
        expected = 11
        result = test_function(list1, list2)
        message = self.explanation(list1, list2, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_2_4_6_and_5_10_15_returns_140(self):
        list1 = [2,4,6]
        list2 = [5,10,15]
        expected = 140
        result = test_function(list1, list2)
        message = self.explanation(list1, list2, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_2_point_5_and_2_point_5_returns_6_point_25(self):
        list1 = [2.5]
        list2 = [2.5]
        expected = 6.25
        result = test_function(list1, list2)
        message = self.explanation(list1, list2, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_1_2_point_5_3_and_1_2_2_point_5_returns_13_point_5(self):
        list1 = [1,2.5,3]
        list2 = [1,2,2.5]
        expected = 13.5
        result = test_function(list1, list2)
        message = self.explanation(list1, list2, expected, result)
        self.assertEqual(expected, result, msg=message)
        
    def test_2_4_6_8_10_and_3_5_7_9_11_returns_250(self):
        list1 = [2,4,6,8,10]
        list2 = [3,5,7,9,11]
        expected = 250
        result = test_function(list1, list2)
        message = self.explanation(list1, list2, expected, result)
        self.assertEqual(expected, result, msg=message)

if __name__ == '__main__':
    unittest.main()