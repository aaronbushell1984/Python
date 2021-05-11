# ***LESSON***

# Create a list syntax - any data type
numbers = [1,2,9,4,33,6]

# Set variable total to zero, loop and add running total to number
# NB. Python uses indents to start and end blocks (not brackets)
# NB. Variables are available outside of loop unlike other languages
total = 0
for number in numbers:
    total += number

print("Total =", total)
languages = ["Python", "Java", "Javascript", "SQL"]

# range function
for number in range(1, 13, 2):
    print("number in range = ", number)

# terminate loop early
for language in languages:
    print(language)
    if language == "Javascript":
        print("Exiting loop early at:", language)
        break
    print("Still in loop")

"""
# ***SLIDES***
# • Repetition statements (or loops) repeat an action
# • Each repetition of action is known as pass or iteration

for eachPass in range(4):
print("It's alive!", end = " ")
#It's alive! It's alive! It's alive! It's alive!

number = 2
exponent = 3
product = 1
for eachPass in range(exponent):
product = product * number
print(product, end=" ")

# Loops that count through a range of numbers:
product = 1
for count in range(4):
product = product * (count + 1)
product

# To specify an explicit lower bound:
product = 1
for count in range(1, 5):
product = product * count
product

# Example: bound-delimited summation
lower = int(input("Enter the lower bound: "))
Enter the lower bound: 1
upper = int(input("Enter the upper bound: "))
Enter the upper bound: 10
theSum = 0
for number in range(lower, upper + 1):
theSum = theSum + number
theSum

Example:
# Count from 1 through 4, we think
for count in range(1,4):
print(count)
#NB. Loop actually counts from 1 through 3

# Traversing the Contents of a Data Sequence
# range returns a sequence of numbers. By converting the sequence to a list we get
list(range(4))
#[0, 1, 2, 3]
list(range(1, 5))
#[1, 2, 3, 4]

Example:
for number in [6, 444 ,8]:
print(number, end=" ")
#6 444 8

# Specifying the Steps in the Range
range expects a third argument that allows you specify a step value:
list(range(1, 6, 1)) # Same as using two arguments
[1, 2, 3, 4, 5]
list(range(1, 6, 2)) # Use every other number
[1, 3, 5]
list(range(1, 6, 3)) # Use every third number
[1, 4]
• Example:
theSum = 0
for count in range(2, 11, 2):
theSum += count
theSum
30

# Loops that Count Down
Example:
for count in range(10, 0, -1):
print(count, end = " ")
# 10 9 8 7 6 5 4 3 2 1
list(range(10, 0, -1))
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Strings and for Loops
# Strings are also sequences of characters
# If a string is passed to a for loop, the string is broken up
# Example:
for character in "Hello!":
print(character)
#H
#e
#l
#l
#o
#!

# Formatting Text for Output 1

# Many data-processing applications require output that has tabular format
# • Field width: Total number of data characters and additional spaces for a datum in a
# formatted string
# • The print function automatically begins printing an output datum in the first available column
for exponent in range(7, 11):
print(exponent, 10 ** exponent)
# 7 10000000
# 8 100000000
# 9 1000000000
# 10 10000000000

# Formatting Text for Output 3/..
# To format data value of type float:
%<field width>.<precision>f
where .<precision> is optional
# Examples:
salary = 100.00
print("Your salary is $" + str(salary))
# Your salary is $100.0
print("Your salary is $%0.2f" % salary)
# Your salary is $100.00
"""