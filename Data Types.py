# ***LESSON***

# Integer Type
my_int_number = 123
print(type(my_int_number))

# Float Type
my_float_number = 12.34
print(type(my_float_number))

# Complex Number Type
my_complex_number = 5j
print(type(my_complex_number))

# Type conversion - loses a unit
what_type = my_int_number / my_float_number
print(type(what_type))

# Addition examples
total = 0
# Long form
total = total + 10
# Short form
total += 10
print("total = ", total)

# Subtraction Example
total -= 10
print("total = ", total)

# Multiply Example
total *= 10
print("total = ", total)

# Divide Example
total /= 10
print("total= ", total)

# Modulus remainder example
remainder = my_int_number % total
print("remainder = ", remainder)

# Maths Library
#NB. IMPORTS SHOULD BE AT TOP OF FILE
import math # MOVE TO LINE 1

# Dot notation for methods on math import
print(math.pi)
print(math.pow(5, 10))

# Precedence Examples
first = 1
second = 2
third = 3
# Bodmas rules makes multiplication happen first
print(first + second * third)
# Clearer to bracket intention - In this case also changes output
print((first + second) * third)

# Decimal Library - import part of library example
#NB. IMPORTS SHOULD BE AT TOP OF FILE
from decimal import Decimal # MOVE TO LINE 2

# Decimal Example
price = Decimal("29.99")
vat = Decimal("20.00") / Decimal("100")
print(vat)
# Decimal keeps more precision than the 16 decimal places that is built in
total = price + (price * vat)
print("Total =", total)

# ***SLIDES***
# Expressions provide easy way to perform operations on data values to produce other values
# BODMAS IS IMPORTANT
"""
Precedence rules:
** has the highest precedence and is evaluated first
Unary negation is evaluated next
*, /, and % are evaluated before + and −
+ and − are evaluated before =
With two exceptions, operations of equal precedence are left associative, so they are evaluated from left to right
** and = are right associative
You can use ( ) to change the order of evaluation
"""

# Math Module requires import
import math
math.pi

math.sqrt(2)

# Importing part of a module example
from math import pi, sqrt
print(pi, sqrt(2))

3 + 4 * \
2 ** 5

# Mixed-mode arithmetic involves integers and floating-point numbers
3.14 * 3 ** 2 # results floating point

# You must use a type conversion function when working with input of numbers
# It is a function with the same name as the data type to which it converts

# Type conversion also occurs in the construction of strings from numbers and other strings
profit = 1000.55
print('$' + str(profit)) # must be declared to string to concatenate

# Functions often require arguments or parameters. eg (round) below - can be optional
def square(x):
   """Returns the square of x."""
   return x * x

# help will give information on the passed parameter
help(round)







