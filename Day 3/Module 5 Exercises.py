# Module 5: Lists and Dictionaries

# 1. Assume that the variable data refers to the list [5, 3, 7] Write the values of the following expressions:
data = [5, 3, 7]

data[2]
# 7

data[-1]
# 7

len(data)
# 3

data[0:2]
# [5, 3]

0 in data
# False

data + [2, 10, 5]
# [5, 3, 7, 2, 10, 5]

tuple(data)
# (5, 3, 7) now a tuple

# 2. Assume that the variable data refers to the list [5, 3, 7] Write the expressions that perform the following tasks:
data1 = [5, 3, 7]
# a. Replace the value at position 0 in data with that value’s negation.
data1[0] = -data1[0]
# b. Add the value 10 to the end of data.
data1.append(10)
# c. Insert the value 22 at position 2 in data.
data1.insert(2, 22)
# d. Remove the value at position 1 in data.
data1.pop(1)

# 3. Define a function named even. This function expects a number as an argument and returns True if the number is divisible by 2, or it returns False otherwise. (Hint: A number is evenly divisible by 2 if the remainder is 0.)
number = int(input("Please enter a number: "))

def is_even(number):
    if number % 2 == 0:
        return print("True")
    else:
        return print("False")

is_even(number)

# 4. Use the function even to create a similar funaction called odd
def is_odd(number):
    number += 1
    is_even(number)
is_odd(number)

# 5. Define a function named summation. This function expects two numbers, named low and high, as arguments. The function computes and returns the sum of the numbers between low and high, inclusive.
low = int(input("Please enter a low number: "))
high = int(input("Please enter a high number: "))
def summation(low, high):
    total = 0
    for count in range(low, high+1):
        total += count
    return total
print(summation(low, high))

# 6. Assume that the variable data refers to the dictionary: {'b':20, 'a':35} Write the values of the following expressions:

data['a']

data.get('c', None)

len(data)

data.keys( )

data.values( )

data.pop('b')

data # After the pop above

# 7. Assume that the variable data refers to the dictionary: {'b':20, 'a':35} Write the expressions that perform the following tasks:

# a. Replace the value at the key 'b' with that value’s negation.

# b. Add the key/value pair 'c':40 to data.

# c. Remove the value at key 'b' in data, safely.

# d. Print the keys in data in alphabetical order.
