"""
Module 5: Lists and Dictionaries

1. Assume that the variable data refers to the list [5, 3, 7] Write the values of the following expressions:

a. data[2]

b. data[-1]

c. len(data)

d. data[0:2]

e. 0 in data

f. data + [2, 10, 5]

g. tuple(data)

2. Assume that the variable data refers to the list [5, 3, 7] Write the expressions that perform the following tasks:

a. Replace the value at position 0 in data with that value’s negation.

b. Add the value 10 to the end of data.

c. Insert the value 22 at position 2 in data.

d. Remove the value at position 1 in data.

3. Define a function named even. This function expects a number as an argument and returns True if the number is divisible by 2, or it returns False otherwise. (Hint: A number is evenly divisible by 2 if the remainder is 0.)

4. Use the function even to create a similar funaction called odd

5. Define a function named summation. This function expects two numbers, named low and high, as arguments. The function computes and returns the sum of the numbers between low and high, inclusive.

6. Assume that the variable data refers to the dictionary: {'b':20, 'a':35} Write the values of the following expressions:

a. data['a']

b. data.get('c', None)

c. len(data)

d. data.keys( )

e. data.values( )

f. data.pop('b')

g. data # After the pop above

7. Assume that the variable data refers to the dictionary: {'b':20, 'a':35} Write the expressions that perform the following tasks:

a. Replace the value at the key 'b' with that value’s negation.

b. Add the key/value pair 'c':40 to data.

c. Remove the value at key 'b' in data, safely.

d. Print the keys in data in alphabetical order.
"""