# Python has Input, Output and Error Streams
# Python executes code sequentially - Line by Line
# Python style guide https://www.python.org/dev/peps/pep-0008/

# Add items to input stream with input - Print variable to output stream
name = input('enter your name: ')
print("Your name is", name)

# Input takes input and outputs as a string by default. To add to age then use int(x) to cast to number
age = int(input("enter your age:"))
print("Your age is", age)

# += adds and assigns to variable in shorthand, -= subtracts and assigns, *= multiplies and assigns
age += 10
print("Your age in a decade will be", age)

# Built-in functions with parameters example
print(max(5,2,9,4))
print(min(5,2,9,4))

# Functions can be assigned to a variable
maximum = print(max(5,2,9,4))
print(maximum)

# Indent blocks - MUST BE INDENTED
if maximum > 8:
    print("maximum is greater than 8")

"""
TO ACCESS PYTHON KEYWORDS -
Enter Python compiler in terminal (type python)
IMPORT A LIBRARY FOR KEYWORD
Enter - import keyword
Enter - print(keyword.kwlist)
'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
"""

# NB. DO NOT USE VARIABLES OR FILE NAMES WITH KEYWORDS
# NB. PYTHON WILL PRODUCE AN INDENT ERROR IF A SPACE PRECEDES FUNCTION
# NB. VARIABLES MUST NOT START WITH A NUMBER, ARE CASE SENSITIVE
# NB. CONVENTION is to_use_variable_with_lowercase_underscores