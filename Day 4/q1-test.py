"""
  #####                                                  #   
 #     # #    # ######  ####  ##### #  ####  #    #     ##   
 #     # #    # #      #        #   # #    # ##   #    # #   
 #     # #    # #####   ####    #   # #    # # #  #      #   
 #   # # #    # #           #   #   # #    # #  # #      #   
 #    #  #    # #      #    #   #   # #    # #   ##      #   
  #### #  ####  ######  ####    #   #  ####  #    #    ##### 
                                                             
 #     #                   #######                            
 #     # #    # # #####       #    ######  ####  #####  ####  
 #     # ##   # #   #         #    #      #        #   #      
 #     # # #  # #   #         #    #####   ####    #    ####  
 #     # #  # # #   #         #    #           #   #        # 
 #     # #   ## #   #         #    #      #    #   #   #    # 
  #####  #    # #   #         #    ######  ####    #    ####  

"""                                                          

FILE = 'q1'
FUNCTION = 'rightAngledTriangle'

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
    from q1 import rightAngledTriangle as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, side1, side2, side3, right_angled, result):
        message = FUNCTION+'('+str(side1)+', '+str(side2)+', '+str(side3)+')'
        message = message+'\n\nTriangle side='+str(side1)+' side='+str(side2)+' side='+str(side3)+' ~ Right Angled: '+str(right_angled)+' - You returned '+str(result)
        return message

    def test_0_0_0_is_false(self):
        side1 = 0
        side2 = 0
        side3 = 0
        right_angled = False
        result = test_function(side1, side2, side3)
        message = self.explanation(side1, side2, side3, right_angled, result)
        self.assertEqual(right_angled, result, msg=message)

    def test_0_1_1_is_false(self):
        side1 = 0
        side2 = 1
        side3 = 1
        right_angled = False
        result = test_function(side1, side2, side3)
        message = self.explanation(side1, side2, side3, right_angled, result)
        self.assertEqual(right_angled, result, msg=message)

    def test_1_1_1_is_false(self):
        side1 = 1
        side2 = 1
        side3 = 1
        right_angled = False
        result = test_function(side1, side2, side3)
        message = self.explanation(side1, side2, side3, right_angled, result)
        self.assertEqual(right_angled, result, msg=message)

    def test_3_4_5_is_true(self):
        side1 = 3
        side2 = 4
        side3 = 5
        right_angled = True
        result = test_function(side1, side2, side3)
        message = self.explanation(side1, side2, side3, right_angled, result)
        self.assertEqual(right_angled, result, msg=message)

    def test_5_4_3_is_true(self):
        side1 = 5
        side2 = 4
        side3 = 3
        right_angled = True
        result = test_function(side1, side2, side3)
        message = self.explanation(side1, side2, side3, right_angled, result)
        self.assertEqual(right_angled, result, msg=message)

    def test_4_5_3_is_true(self):
        side1 = 4
        side2 = 5
        side3 = 3
        right_angled = True
        result = test_function(side1, side2, side3)
        message = self.explanation(side1, side2, side3, right_angled, result)
        self.assertEqual(right_angled, result, msg=message)

    # test if side1*2 rather than side1**2
    def test_3_4_7_is_false(self):
        side1 = 3
        side2 = 4
        side3 = 7
        right_angled = False
        result = test_function(side1, side2, side3)
        message = self.explanation(side1, side2, side3, right_angled, result)
        self.assertEqual(right_angled, result, msg=message)

    def test_9_16_25_is_false(self):
        side1 = 9
        side2 = 16
        side3 = 25
        right_angled = False
        result = test_function(side1, side2, side3)
        message = self.explanation(side1, side2, side3, right_angled, result)
        self.assertEqual(right_angled, result, msg=message)

    def test_5_12_13_is_true(self):
        side1 = 5
        side2 = 12
        side3 = 13
        right_angled = True
        result = test_function(side1, side2, side3)
        message = self.explanation(side1, side2, side3, right_angled, result)
        self.assertEqual(right_angled, result, msg=message)

    def test_right_angled_triangle_with_sides_8_17_15_is_true(self):
        side1 = 8
        side2 = 17
        side3 = 15
        right_angled = True
        result = test_function(side1, side2, side3)
        message = self.explanation(side1, side2, side3, right_angled, result)
        self.assertEqual(right_angled, result, msg=message)

    def test_60_61_11_is_true(self):
        side1 = 60
        side2 = 61
        side3 = 11
        right_angled = True
        result = test_function(side1, side2, side3)
        message = self.explanation(side1, side2, side3, right_angled, result)
        self.assertEqual(right_angled, result, msg=message)

    def test_60_60_10_is_false(self):
        side1 = 60
        side2 = 60
        side3 = 10
        right_angled = False
        result = test_function(side1, side2, side3)
        message = self.explanation(side1, side2, side3, right_angled, result)
        self.assertEqual(right_angled, result, msg=message)


if __name__ == '__main__':
    unittest.main()
