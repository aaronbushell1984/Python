"""
  #####                                                 #####  
 #     # #    # ######  ####  ##### #  ####  #    #    #     # 
 #     # #    # #      #        #   # #    # ##   #          # 
 #     # #    # #####   ####    #   # #    # # #  #     #####  
 #   # # #    # #           #   #   # #    # #  # #          # 
 #    #  #    # #      #    #   #   # #    # #   ##    #     # 
  #### #  ####  ######  ####    #   #  ####  #    #     #####  
                                                               
 #     #                   #######                            
 #     # #    # # #####       #    ######  ####  #####  ####  
 #     # ##   # #   #         #    #      #        #   #      
 #     # # #  # #   #         #    #####   ####    #    ####  
 #     # #  # # #   #         #    #           #   #        # 
 #     # #   ## #   #         #    #      #    #   #   #    # 
  #####  #    # #   #         #    ######  ####    #    ####  

"""

FILE = 'q3'
FUNCTION = 'countWords'

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
    from q3 import countWords as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, string, count, result):
        s = '' if count == 1 else 's'
        message = FUNCTION+'("'+string+'")'
        message = message+'\n\nThe string "'+string+'" has '+str(count)+' word'+s+' ending in r or s - You returned '+str(result)
        return message

    def test_empty_string(self):
        string = ''
        count = 0
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)

    def test_double_quote_has_0_words(self):
        string = '"'
        count = 0
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)

    def test_double_quotes_has_0_words(self):
        string = '""'
        count = 0
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)

    def test_single_quote_has_0_words(self):
        string = "'"
        count = 0
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)

    def test_single_quotes_has_0_words(self):
        string = "''"
        count = 0
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)

    def test_convert_to_lower_case(self):
        string = 'PAPER CHASE'
        count = 1
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)

    def test_special_characters(self):
        string = '!"£ $%^ &*( )-=1,234 56789 0-=ABC PQRs tuv  '
        count = 1
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)

    def test_Ar_Ar_As_Ra_Ra_Sa_has_3_words(self):
        string = 'Ar Ar As Ra Ra Sa'
        count = 3
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)

    def test_just_spaces(self):
        string = '          '
        count = 0
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)

    def test_multiple_spaces(self):
        string = ' s   ss  r   x      rr'
        count = 4
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)

    def test_sss_rrrrr_abcdef_has_2_words(self):
        string = 'sss rrrrr abcdef'
        count = 2
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)

    def test_red_paper_files_has_2_words(self):
        string = 'red paper files'
        count = 2
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)

    def test_paper_chase_has_1_word(self):
        string = 'paper chase'
        count = 1
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)

    def test_rr_RR_ss_SS_has_4_words(self):
        string = 'rr RR ss SS'
        count = 4
        result = test_function(string)
        message = self.explanation(string, count, result)
        self.assertEqual(count, result, msg=message)


if __name__ == '__main__':
    unittest.main()
