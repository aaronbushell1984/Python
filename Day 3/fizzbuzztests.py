import fizzbuzz
import unittest

class fizzbuzztests(unittest.TestCase):

    def test_when_number_3_result_true(self):
        self.assertTrue(fizzbuzz.is_fizz(3))

    def test_when_number_27_result_true(self):
        self.assertTrue(fizzbuzz.is_fizz(27))

    def test_when_number_1_result_false(self):
        self.assertFalse(fizzbuzz.is_fizz(1))

    def test_when_number_0_result_true(self):
        self.assertTrue(fizzbuzz.is_fizz(0))

    def test_when_number_minus_3_result_true(self):
        self.assertTrue(fizzbuzz.is_fizz(-3))

    def test_when_number_15_result_FizzBuzz(self):
        self.assertEqual("FizzBuzz", fizzbuzz.apply_fizz_buzz_rules(15))
    
    def test_when_number_1_result_not_FizzBuzz(self):
        self.assertEqual("1 is not FizzBuzz", fizzbuzz.apply_fizz_buzz_rules(1))

    

if __name__ == "__main__":
    unittest.main(exit=False)