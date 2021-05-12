# ***LESSON***

# Rewrite this function into reusable functions
number = int(input("Please enter a number:"))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
# Rewrite to
def is_fizz(number):
    """returns if the number is divisible by 3"""
    return number % 3 == 0

def is_buzz(number):
    """returns if the number is divisible by 5"""
    return number % 5 == 0

def is_fizz_buzz(number):
    """returns if the number is divisible by 3 and 5"""
    return is_fizz and is_buzz

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






# ***SLIDES***

# Definition of a function consists of header and body
def square(x):
    """Returns the square of x."""
    return x * x
# • Docstring contains information about what the function does; to display, enter:
help(square)

# NB FUNCTIONS MUST BE DECLARED BEFORE USED
# A Boolean function usually tests its argument for the presence or absence of some property
# • Returns True if property is present; False otherwise
# • Example:
def odd(x):
    """ Returns True if x is odd or False otherwise."""
    if x % 2 == 1:
        return True
    else:
        return False
odd(5)
# True
odd(6)
# False

# main serves as the entry point for a script
"""Illustrates the definition of a main function."""
def main( ):
    """The main function for this script."""
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)
def square(x):
    """Returns the square of x"""
    return x * x
# The entry point for program execution
main() # There is a new way of doing this...
