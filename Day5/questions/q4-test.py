
FILE = 'q4'
FUNCTION = 'rock_paper_scissors'

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
    from q4 import rock_paper_scissors as test_function
except:
    print('The function "'+FUNCTION+'" has syntax errors!')
    print('\nFAILED (errors=1)')
    print('------------------------------------------------------------------')
    sys.exit(4)


class UnitTestCase(unittest.TestCase):

    # Only show custom message
    def setUp(self):
        self.longMessage = False

    def explanation(self, choice1, choice2, expected, result):
        message = FUNCTION+'('+choice1+','+choice2+')'
        message = message+'\n\nThe result of '+choice1+' vs '+choice2+' is '+expected+'\n - You returned '+result
        if not isinstance(result, str):
            message = message+'\n\nReturned value must be a string'
        return message

    def test_empty_returns_invalid_choice(self):
        choice1 = ''
        choice2 = 'rock'
        expected = 'Invalid choice'
        result = test_function(choice1, choice2)
        message = self.explanation(choice1, choice2, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_invalid_choice(self):
        choice1 = 'rock'
        choice2 = 'lizard'
        expected = 'Invalid choice'
        result = test_function(choice1, choice2)
        message = self.explanation(choice1, choice2, expected, result)
        self.assertEqual(expected, result, msg=message)
        
    def test_rock_and_rock_returns_tie(self):
        choice1 = 'rock'
        choice2 = 'rock'
        expected = 'Tie'
        result = test_function(choice1, choice2)
        message = self.explanation(choice1, choice2, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_case_insensitivity(self):
        choice1 = 'ROCK'
        choice2 = 'rock'
        expected = 'Tie'
        result = test_function(choice1, choice2)
        message = self.explanation(choice1, choice2, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_rock_and_scissors_returns_player_1_win(self):
        choice1 = 'rock'
        choice2 = 'scissors'
        expected = 'Player 1 wins'
        result = test_function(choice1, choice2)
        message = self.explanation(choice1, choice2, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_rock_and_paper_returns_player_2_win(self):
        choice1 = 'rock'
        choice2 = 'paper'
        expected = 'Player 2 wins'
        result = test_function(choice1, choice2)
        message = self.explanation(choice1, choice2, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_paper_and_rock_returns_player_1_win(self):
        choice1 = 'paper'
        choice2 = 'rock'
        expected = 'Player 1 wins'
        result = test_function(choice1, choice2)
        message = self.explanation(choice1, choice2, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_paper_and_scissors_returns_player_2_win(self):
        choice1 = 'paper'
        choice2 = 'scissors'
        expected = 'Player 2 wins'
        result = test_function(choice1, choice2)
        message = self.explanation(choice1, choice2, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_scissors_and_paper_returns_player_1_win(self):
        choice1 = 'scissors'
        choice2 = 'paper'
        expected = 'Player 1 wins'
        result = test_function(choice1, choice2)
        message = self.explanation(choice1, choice2, expected, result)
        self.assertEqual(expected, result, msg=message)

    def test_scissors_and_rock_returns_player_2_win(self):
        choice1 = 'scissors'
        choice2 = 'rock'
        expected = 'Player 2 wins'
        result = test_function(choice1, choice2)
        message = self.explanation(choice1, choice2, expected, result)
        self.assertEqual(expected, result, msg=message)

if __name__ == '__main__':
    unittest.main()