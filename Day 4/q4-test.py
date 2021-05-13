"""
  #####                                                #       
 #     # #    # ######  ####  ##### #  ####  #    #    #    #  
 #     # #    # #      #        #   # #    # ##   #    #    #  
 #     # #    # #####   ####    #   # #    # # #  #    #    #  
 #   # # #    # #           #   #   # #    # #  # #    ####### 
 #    #  #    # #      #    #   #   # #    # #   ##         #  
  #### #  ####  ######  ####    #   #  ####  #    #         #  
                                                               
 #     #                   #######                            
 #     # #    # # #####       #    ######  ####  #####  ####  
 #     # ##   # #   #         #    #      #        #   #      
 #     # # #  # #   #         #    #####   ####    #    ####  
 #     # #  # # #   #         #    #           #   #        # 
 #     # #   ## #   #         #    #      #    #   #   #    # 
  #####  #    # #   #         #    ######  ####    #    ####  

"""

FILE = 'q4'
FUNCTION = 'findDuplicates'

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
    from q4 import findDuplicates as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, string, duplicates, result):
        s = '' if duplicates == 1 else 's'
        message = FUNCTION+'("'+string+'")'
        message = message+'\n\nThe string "'+str(string)+'" has '+str(duplicates)+' duplicate'+s+' - You returned '+str(result)
        return message

    def test_empty_string_returns_0(self):
        string = ''
        duplicates = 0
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)

    def test_double_quote_returns_0(self):
        string = '"'
        duplicates = 0
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)

    def test_double_quotes_returns_1(self):
        string = '""'
        duplicates = 1
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)

    def test_single_quote_returns_0(self):
        string = "'"
        duplicates = 0
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)

    def test_single_quotes_returns_1(self):
        string = "''"
        duplicates = 1
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)

    def test_bbca_returns_1(self):
        string = 'bbca'
        duplicates = 1
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)

    def test_bccbbbbbb_returns_2(self):
        string = 'bccbbbbbb'
        duplicates = 2
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)

    def test_abcdef_returns_0(self):
        string = 'abcdef'
        duplicates = 0
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)

    def test_zAABBcd_returns_2(self):
        string = 'zAABBcd'
        duplicates = 2
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)

    def test_11223344_returns_5(self):
        string = ' 111111222222333333444444 '
        duplicates = 5
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)

    def test_HGF_hgf_returns_0(self):
        string = 'HGF hgf'
        duplicates = 0
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)

    def test_hashhash12ab_returns_1(self):
        string = '##12ab'
        duplicates = 1
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)

    def test_special_chars_returns_7(self):
        string = "12345 abc 12345 !'£$%^&*()_+\/'"
        duplicates = 7
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)
        
    def test_260_characters_returns_26(self):
        string = 'abcDEFghiJKLmnoPQRstuVWXyz'*5
        duplicates = 26
        result = test_function(string)
        message = self.explanation(string, duplicates, result)
        self.assertEqual(duplicates, result, msg=message)


if __name__ == '__main__':
    unittest.main()
