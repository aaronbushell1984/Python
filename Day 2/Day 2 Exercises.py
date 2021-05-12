# 1.     Write a program that prompts the user for 3 numbers and then returns the largest of the 3 	numbers. Do this without using the max() function – write an IF statement.
first = int(input("Please enter your first number:"))
second = int(input("Please enter your second number:"))
third = int(input("Please enter your third number:"))
if first > second and first > third:
    print("Your first number is largest")
if second > first and second > third:
    print("Your second number is largest")
if third > first and third > second:
    print("Your third number is largest")

# 2.	Prompt the user to input a number.
		#If the number is divisible by 3, print Fizz.
		# If the number is divisible by 5, print Buzz.
		# If the number is divisible by both 3 and 5 print FizzBuzz.
		# Otherwise, print the number.
number = int(input("Please enter a number:"))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

# 3.	Prompt the user to input a number.
		# If the number is between 1 and 10, print Number is in range.
		# If the number is 0 or larger than 10, print Number is outside range.
		# If the number is negative, print Number cannot be negative.
number = int(input("Please enter a number:"))
if number < 0:
    print("Number cannot be negative")
elif number < 10 or number > 1:
    print("Number is in range")
else:
    print("Number is outside range")

# 4.	Create a dictionary of various makes and models of vehicles.
	# Use your dictionary to print a series of statements about each of these vehicles.
	# e.g. "I would like to own a Rolls-Royce Silver Wraith",
	# "I would like to own a Massey Ferguson Combine Harvester" etc.
car_dictionary = {
  "brand": ["Ford", "Rolls Royce", "Massey Ferguson"],
  "model": ["Mustang", "Silver Wraith", "Combine Harvester"]
}

print("I would like to own a", car_dictionary["brand"][1], car_dictionary["model"][1])
print("I would like to own a", car_dictionary["brand"][2], car_dictionary["model"][2])

# 5.	Print the whole numbers from 0-10 using a WHILE loop.
number = 0
while True:
    if number >= 0 and number < 11:
        print(number)
        number += 1
    else:
        break

# 6.	Print just the odd numbers from 1-20 using a FOR loop.
for number in range(20):
    if number % 2 != 0:
        print(number)

# 7.	Starting at 3, print the numbers that are multiples of 3, up to and including 30, using a 	WHILE loop.
number = 3
while number <= 30 and number >= 3:
    if number % 3 == 0:
        print(number)
    number += 1

# 8.	Accept a number from the user and calculate the sum of all the numbers between 1 and the 	input number. For example, if the user inputs 10, the output should be 55.
the_sum = 0
number = int(input("Please enter a number:"))
for number in range(1, number+1):
    the_sum += number
print(the_sum)


# 9.	Write a program to print the following pattern:
"""
		*
		**
		***
		****	
		*****
"""

for exponent in range(1, 6):
    print("*" * exponent)

# 10.	Modify your code from Exercise 9 to accept a number from the user to determine how 	many rows are output.
number = int(input("Please enter a number:"))
for exponent in range(1, number+1):
    print("*" * exponent)

# Questions from Module 3
# 8. Assume that the variables x and y refer to strings. Write a code segment that prints these strings in alphabetical order. You should assume that they are not equal.
x = input("Please enter your first word: ")
y = input("Please enter your second word: ")
if x > y:
    print(y, x)
else:
    print(x, y)

# The variables x and y refer to numbers. Write a code segment that prompts the user for an arithmetic operator and prints the value obtained by applying that operator to x and y
total = 0
x = int(input("Please enter a number:"))
y = int(input("Please enter a number:"))
operator = input("Please enter and arithmetic operator")
while operator:
    if operator == "+":
        total = x + y
    elif operator == "-":
        total = x - y
        break
print(total)


