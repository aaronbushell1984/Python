# ***LESSON***

# Validates if between 1 and 9 and then runs - Common mistake - wont't run
counter = 0
while counter <= 10 and counter > 0:
    counter += 1
    print(counter)
# This will run instead
counter = 1
while counter <= 10 and counter > 0:
    counter += 1
    print(counter)

# Infinite Loop
while True:
    response = int(input("eneter a number:"))
    if response % 7 == 0:
        print("number is divisible by 7")
        break
    else:
        print("number is not divisible by the lucky number")

# ***SLIDES***

# Conditional Iteration: The while Loop
# Conditional iteration requires that condition be tested within loop to determine if it should continue
# NB. IMPROPER USE MAY LEAD TO INFINITE LOOP

# Example:
theSum = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or just enter to quit: ")
print("The sum is", theSum)
# Enter a number or just enter to quit: 3
# Enter a number or just enter to quit: 4
# Enter a number or just enter to quit: 5
# Enter a number or just enter to quit:
# The sum is 12.0

# You can use a while loop for a count-controlled loop instead of a for loop:
# Summation with a for loop
theSum = 0
for count in range(1, 100001):
    theSum += count
print(theSum)
# Summation with a while loop
theSum = 0
count = 1
while count <= 100000:
    theSum += count
    count += 1
print(theSum)

# The while loop can be complicated to write correctly
# • It is possible to simplify its structure and improve its readability
theSum = 0.0
while True:
    data = input("Enter a number or just enter to quit: ")
    if data == "":
        break
    number = float(data)
    theSum += number

print("The sum is", theSum)

# This example modifies the input section of the grade-conversion program to continue taking
# input numbers from the user until entering an acceptable value:
while True:
    number = int(input("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
        break
    else:
        print("Error: grade must be between 100 and 0")
print(number) # Just echo the valid input

# Alternative: Use a Boolean variable to control loop
done = False
while not done:
    number = int(input("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
        done = True
    else:
        print("Error: grade must be between 100 and 0")

print(number) # Just echo the valid input

# Random Numbers
# Example: A simple guessing game (guess.py)
import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else:
        print("Congratulations! You've got it in", count, "tries!")
        break
