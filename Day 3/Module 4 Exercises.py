# Module 4: Strings and Text Files

# 1. Assume that the variable data refers to the string # "myprogram.exe". Write the values of the following expressions:

# a. data[2]
# p

# b. data[-1]
# e

# c. len(data)
# 13

# d. data[0:8]
# myprogra

# 2. Assume that the variable data refers to the string # "myprogram.exe". Write the expressions that perform the following tasks:
data = "myprogram.exe"
# a. Extract the substring "gram" from data.
data[5:9]
# b. Truncate the extension ".exe" from data.
data[-4:]
# c. Extract the character at the middle position from data.
data[(len(data)-1)//2:(len(data)+2)//2]

# 3. Assume that the variable myString refers to a string. # Write a code segment that uses a loop to print the characters of the string in reverse order.
my_string = "banana"
for index in range(len(my_string)-1, -1, -1):
    print(my_string[index])

# 4. Assume that the variable myString refers to a string, and the variable reversedString refers to an empty string. Write a loop that adds the characters from myString to reversedString in reverse order.
my_string = "banana"
my_reversed_string = ""
for index in range(len(my_string)-1, -1, -1):
    my_reversed_string += my_string[index]
print(my_string)
print(my_reversed_string)

""" NB DO NOT USE THESE CYPHERS
# 5. Write the encrypted text of each of the following words using a Caesar cipher with a distance value of 3:

a. python

b. hacker

c. wow


6. You are given a string that was encoded by a Caesar cipher with an unknown distance value. The text can contain any of the printable ASCII characters. Suggest an algorithm for cracking this code.
"""