# ***LESSON***

value = True
if value: # shorthand for booleans of if value = true
    print("value is False")
else:
    print("value is True")

# if, elif and else
number = 33
if number < 0:
    print("Error: number less than 0")
elif number > 100:
    print("Error: number greater than 100")
elif number == 1 or number == 99:
    print("You are a winner")
else:
    print("Bad luck, try again")

# Using a sequence and in/not in
sequence = [1,2,3,7,8,9]
if 4 not in sequence:
    print("4 not present")
else:
    print("found 4")

# Elif with sequence and when it exucutes and doesn't
sequence = [1,2,3,7,8,9]
if 4 not in sequence:
    print("4 not present")
elif 3 in sequence:  
    print("found 3") # This code may not execute if 4 is present
sequence = [1,2,3,7,8,9]
# This will check for both 3 present and 4 not present...
if 4 not in sequence:
    print("4 not present")   
if 3 in sequence:
    print("found 3")

# ***SLIDES***

#If-Else Statements
#• Also called a two-way selection statement
#• Often used to check inputs for errors:
import math
area = float(input("Enter the area: "))
if area > 0:
    radius = math.sqrt(area / math.pi)
    print("The radius is", radius)
else:
    print("Error: the area must be a positive number")

# Multi-Way If Example:
print("Enter numeric grade:")
number = int(input( ))
if number >= 70:
    letter = 'A'
elif number >= 60:
    letter = 'B'
elif number >= 50:
    letter = 'C'
else:
    letter = 'F'

print("Letter grade is", letter)
# NB. It is better to initialise a default (of f for example)

# Longer example...
number = int(input("Numeric grade: "))
if number > 100:
    print("Must be between 100 and 0")
elif number < 0:
    print("Must be between 100 and 0")
else:
    print("Print Something")
# Can be simplified to...
number = int(input("Numeric grade: "))
if number > 100 or number < 0:
    print("Must be between 100 and 0")
else:
    print("Print Something")

# Short-Circuit Evaluation
# • In (A and B), if A is false, then so is the expression, and there is no need to evaluate B
# • In (A or B), if A is true, then so is the expression, and there is no need to evaluate B
# • Short-circuit evaluation: Evaluation stops as soon as possible
# • Example:
count = int(input("Enter the count: "))
theSum = int(input("Enter the sum: "))
if count > 0 and (theSum / count) > 10:
        print("average > 10")
else:
    print("count = 0 or average <= 10")
