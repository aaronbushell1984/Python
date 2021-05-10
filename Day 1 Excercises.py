import math

# 2.	Write a Python program that prints (displays) your name, address, and telephone number.
# 3.	Evaluate the following code at a shell prompt:
#Then assign name an appropriate value, and evaluate the statement again. -COMBINED ANSWER
name = input('enter your name: ')
address = input('enter your address: ')
telephone = int(input('enter your telephone: '))
print("Your name is", name)
print("Your address is", address)
print("Your telephone is", telephone)

#4.	Open an IDLE window, and enter the program below that computes the area of a rectangle. Load the program into the shell by pressing the F5 key, and correct any errors that occur.
#Test the program with different inputs by running it at least three times.

width = int(input("Enter the width: "))
height = int(input("Enter the height: "))
area = width * height
print("The area is", area, "square units")

# 5.	Modify the program of Exercise 4 to compute the area of a triangle. Issue the appropriate prompts for the triangle's base and height, and change the names of the variables appropriately. Then, use the formula:
base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
area = 0.5 * base * height 
print("The area is", area, "square units")

#to compute the area. Test the program from an IDLE window.
# 6.	Write and test a program that computes the area of a circle. This program should request a number representing a radius as input from the user.
#It should use the formula:
#3.14 * radius ** 2
#to compute the area and then output this result suitably labeled.
radius = int(input("Enter the radius: "))
area = math.pi * radius ** 2
print("The area is", area, "square units")

# 7.	Write and test a program that accepts the user's name (as text) and age (as a number) as input. The program should output a sentence containing the user's name and age.
name = input('enter your name: ')
age = int(input('enter your age: '))
print("Your name is", name + " and your age is", age)

# 8.	Write a line of code using the input function at the shell prompt. When the prompt asks you for input, enter your first name.  Now write the same statement but assign it to a variable called myName
input('enter your name: ')
myName = input('enter your name: ')

# 9.	Write some code using the input function at the shell prompt. Don’t use the int( ) function. When the prompt asks you for input, enter a number.
number = input("enter number:")

#Then, attempt to add 1 to that number, observe the results, and explain what happened.
number += 1 #TypeError: can only concatenate str (not "int") to str - a string not a number

# 10.	Rewrite the code from the question above and fix it so that it does not produce an error when you add 1 to a number that you entered.
number = int(input('enter your number: '))
number += 1

# 11.	Enter the expression help( ) at the shell prompt. Follow the instructions to browse the topics and modules.
help() # navigate by typing topics etc
help(str)

# 1.	Let the variable x be "dog" and the variable y be "cat".
x = "dog"
y = "cat"

#Write the values returned by the following operations:
#a.	x + y
print(x + y) #dogcat

#b.	"the " + x + " chases the " + y
print("the ", x + " chases the ", y) #the  dog chases the  cat - spaces errors

#c.	x * 4
print(x * 4) #dogdogdogdog

# 2.	Write a string that contains your name and address on separate lines using embedded newline characters. Then write the same string literal without the newline characters.
print("""54 Wandesford
Gosport""")
print("54 Wandesford Gosport")

# 3.	Write a print statement that includes an apostrophe within a string.
print("isn't")
print('isn\'t')

# 4.	Which of the following are valid variable names?
#a.	 length - VALID
#b.	 _width - AVOID - SPECIAL CASE
#c.	 firstBase - CAMELCASE ACEPTABLE if local convention - USUALLY first_base
#d.	 2MoreToGo - INVALID number start
#e.	 halt! NOT ALLOWED

# 5.	Which data type would most appropriately be used to represent the following data values?
#a.	 The number of months in a year INTEGER
#b.	 The area of a circle FLOATING POINT
#c.	 The current minimum wage FLOATING POINT or STRING
#d.	 The approximate age of the universe (12,000,000,000 years) INTEGER
#e.	 Your name STRING

# 6.	Explain the differences between the data types int and float.
# Float has decimals
# Integer is a dingle value

# 7.	Write the values of the following scientific notation numbers:
#a.	 3.5576e2 355.76
#b.	 7.832e-3 0.007832
#c.	 4.3212e0 4.3212

# 9.	Let x = 8 and y = 2. Write the values of the following expressions:
x = 8
y = 2

#a.	 x + y * 3
print(x + y * 3) # 14

#b.	 (x + y) * 3
print((x + y) * 3) # 30

#c.	 x ** y
print(x ** y) # 64

#d.	 x % y
print(x % y) # 0

#e.	 x / 12.0
print(x / 12.0) # 0.6666666666666666

#f.	 x // 6
print(x // 6) # 1

# 10.	Let x = 4.66 Write the values of the following expressions:
x = 4.66

#a.	 round(x)
print(round(x)) # 5

#b.	 int(x)
print(int(x)) # 4

# 11.	How does a Python programmer round a float value to the nearest int value?
float = 1.7777
round(float)

# 12.	How does a Python programmer concatenate a numeric value to a string value?
print("Concatenate to the number: ", float)
# option
print("Concatenate to the number: ", str(float))

# 13.	Assume that the variable x has the value 55. 
#Use an assignment statement to increment the value of x by 1.
x = 55
x += 1
print(x)