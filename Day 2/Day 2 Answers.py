# 1.     Write a program that prompts the user for 3 numbers and then returns the largest of the 3 	numbers. Do this without using the max() function – write an IF statement.
number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

if number1 > number2:
    if number1 > number3:
        print(f"Maximum: {number1}")
elif number2 > number3:
    print(f"Maximum: {number2}")
else:
    print(f"Maximum: {number3}")

# 2.	Prompt the user to input a number.
		#If the number is divisible by 3, print Fizz.
		# If the number is divisible by 5, print Buzz.
		# If the number is divisible by both 3 and 5 print FizzBuzz.
		# Otherwise, print the number.
def isfizz(number):
    return number % 3 == 0

def isBuzz(number):
    return number % 5 == 0

def isFizzBuzz(number):
    return isfizz(number) and isBuzz(number)

def applyFizzBuzzRules(number):
    if isFizzBuzz(number):
        return "FizzBuzz"
    elif isfizz(number):
        return "Fizz"
    elif isBuzz(number):
        return "Buzz"
    else:
        return str(number)

# 3.	Prompt the user to input a number.
		# If the number is between 1 and 10, print Number is in range.
		# If the number is 0 or larger than 10, print Number is outside range.
		# If the number is negative, print Number cannot be negative.
number = int(input("Enter a number: "))


if number >= 0:
    if number in range(1,10):
        print("Number is in range")
    else:
        print("Number is outside range")
else:
    print("Number cannot be negative")

# 4.	Create a dictionary of various makes and models of vehicles.
	# Use your dictionary to print a series of statements about each of these vehicles.
	# e.g. "I would like to own a Rolls-Royce Silver Wraith",
	# "I would like to own a Massey Ferguson Combine Harvester" etc.
favourite_vehicles = {
    "Aventador"     :   "Lamborghini",
    "Electra Glide" :   "Harley-Davidson",
    "Tractor"       :   "John Deere"
    }

for key, value in favourite_vehicles.items():
    print(f"I would like to own a {value} {key}")

# 5.	Print the whole numbers from 0-10 using a WHILE loop.
i = 0
while i <= 10:
    print(i)
    i += 1

# 6.	Print just the odd numbers from 1-20 using a FOR loop.
for i in range(1,21,2):
    print(i)

# 7.	Starting at 3, print the numbers that are multiples of 3, up to and including 30, using a 	WHILE loop.
i = 3

while i < 31:
    print(i)
    i += 3

# 8.	Accept a number from the user and calculate the sum of all the numbers between 1 and the 	input number. For example, if the user inputs 10, the output should be 55.
total = 0
number = int(input("Enter a number: "))

for i in range(1, number+1):
    total += i
print(total)


# 9.	Write a program to print the following pattern:
"""
		*
		**
		***
		****	
		*****
"""

star = "*"
output = ""

for i in range(1, 6):
    output = output + star
    print(output)

# 10.	Modify your code from Exercise 9 to accept a number from the user to determine how 	many rows are output.
star = "*"
output = ""
limit = int(input("Enter number of rows required: "))

for i in range(1, limit + 1):
    output = output + star
    print(output)

# Modify your "FizzBuzz" code to loop through
# all the numbers between 1 and 50, replacing numbers
# divisible by 3 with "Fizz", numbers divisible by 5 with "Buzz",
# and numbers divisible by both 3 and 5 with "FizzBuzz".
for number in range(1, 51):    
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)