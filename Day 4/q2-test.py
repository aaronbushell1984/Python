"""
  #####                                                 #####  
 #     # #    # ######  ####  ##### #  ####  #    #    #     # 
 #     # #    # #      #        #   # #    # ##   #          # 
 #     # #    # #####   ####    #   # #    # # #  #     #####  
 #   # # #    # #           #   #   # #    # #  # #    #       
 #    #  #    # #      #    #   #   # #    # #   ##    #       
  #### #  ####  ######  ####    #   #  ####  #    #    ####### 
                                                               
 #     #                   #######                            
 #     # #    # # #####       #    ######  ####  #####  ####  
 #     # ##   # #   #         #    #      #        #   #      
 #     # # #  # #   #         #    #####   ####    #    ####  
 #     # #  # # #   #         #    #           #   #        # 
 #     # #   ## #   #         #    #      #    #   #   #    # 
  #####  #    # #   #         #    ######  ####    #    ####  

"""

FILE = 'q2'
FUNCTION = 'calculateFactorial'

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
    from q2 import calculateFactorial as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, N, factorial, result):
        message = FUNCTION+'('+str(N)+')'
        message = message+'\n\nThe factorial of '+str(N)+' is '+str(factorial)+' - You returned '+str(result)
        return message

    def test_factorial_of_0_is_1(self):
        N = 0
        factorial = 1
        result = test_function(N)
        message = self.explanation(N, factorial, result)
        self.assertEqual(factorial, result, msg=message)

    def test_factorial_of_1_is_1(self):
        N = 1
        factorial = 1
        result = test_function(N)
        message = self.explanation(N, factorial, result)
        self.assertEqual(factorial, result, msg=message)

    def test_factorial_of_2_is_2(self):
        N = 2
        factorial = 2
        result = test_function(N)
        message = self.explanation(N, factorial, result)
        self.assertEqual(factorial, result, msg=message)

    def test_factorial_of_3_is_6(self):
        N = 3
        factorial = 6
        result = test_function(N)
        message = self.explanation(N, factorial, result)
        self.assertEqual(factorial, result, msg=message)

    def test_factorial_of_4_is_24(self):
        N = 4
        factorial = 24
        result = test_function(N)
        message = self.explanation(N, factorial, result)
        self.assertEqual(factorial, result, msg=message)

    def test_factorial_of_5_is_120(self):
        N = 5
        factorial = 120
        result = test_function(N)
        message = self.explanation(N, factorial, result)
        self.assertEqual(factorial, result, msg=message)

    def test_factorial_of_10_is_3628800(self):
        N = 10
        factorial = 3628800
        result = test_function(N)
        message = self.explanation(N, factorial, result)
        self.assertEqual(factorial, result, msg=message)

    def test_factorial_of_12_is_479001600(self):
        N = 12
        factorial = 479001600
        result = test_function(N)
        message = self.explanation(N, factorial, result)
        self.assertEqual(factorial, result, msg=message)

    def test_factorial_of_15_is_1307674368000(self):
        N = 15
        factorial = 1307674368000
        result = test_function(N)
        message = self.explanation(N, factorial, result)
        self.assertEqual(factorial, result, msg=message)

    def test_factorial_of_20_is_2432902008176640000(self):
        N = 20
        factorial = 2432902008176640000
        result = test_function(N)
        message = self.explanation(N, factorial, result)
        self.assertEqual(factorial, result, msg=message)


if __name__ == '__main__':
    unittest.main()
