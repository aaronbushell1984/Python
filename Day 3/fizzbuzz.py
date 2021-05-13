def is_fizz(number):
    """returns if the number is divisible by 3"""
    return number % 3 == 0

def is_buzz(number):
    """returns if the number is divisible by 5"""
    return number % 5 == 0

def is_fizz_buzz(number):
    """returns if the number is divisible by 3 and 5"""
    return is_fizz(number) and is_buzz (number)

def apply_fizz_buzz_rules(number):
    """checks divisible by 3, 5 or both and returns Fizz and Buzz accordingl"""
    if is_fizz_buzz(number):
        return "FizzBuzz"
    elif is_fizz(number):
        return "Fizz"
    elif is_buzz(number):
        return "Buzz"
    else:
        return f"{number} is not FizzBuzz"