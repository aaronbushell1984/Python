# ***LESSON***

# ***SLIDES***

# Some examples:
# ['apples', 'oranges', 'cherries']
# [[5, 9], [541, 78]]
# • When an element is an expression, its value is included in the list:
import math
x = 2
[x, math.sqrt(x)]
[2, 1.4142135623730951]
[x + 1]
[3]

# • Lists of integers can be built using range:
first = [1, 2, 3, 4]
second = list(range(1, 5))
# first
[1, 2, 3, 4]
# second
[1, 2, 3, 4]
# • The list function can build a list from any iterable sequence of elements:
third = list("Hi there!")
# third
['H','i', ' ', 't', 'h', 'e', 'r', 'e', '!']

# len, [ ], +, and == work on lists as expected:
len(first)
# 4
first[0]
# 1
first[2:4]
# [3, 4]
# • Concatenation + and equality = = also work as expected for lists:
first + [5, 6]
# [1, 2, 3, 4, 5, 6]
first == second
# True

# To print the contents of a list:
print("1234")
# 1234
print([1, 2, 3, 4])
# [1, 2, 3, 4]
# in detects the presence of an element:
3 in [1, 2, 3]
# True
0 in [1, 2, 3]
# False

#• A list is mutable
#• Elements can be inserted, removed, or replaced
#• The list itself maintains its identity, but its state (its length and its contents) can change

# Subscript operator is used to replace an element:
example = [1, 2, 3, 4]
print(example)
# [1, 2, 3, 4]
example[3] = 0
print(example)
[1, 2, 3, 0]

# The first session shows how to replace each number in a list with its square:
numbers = [2, 3, 4, 5]
print(numbers)
# [2, 3, 4, 5]
for index in range(len(numbers)):
    numbers[index] = numbers[index] ** 2
print(numbers)
# [4, 9, 16, 25]

# The code below uses the string method split to extract a list of words:
sentence = "This example has 5 words."
words = sentence.split()
print(words)
# ['This', 'example', 'has', '5', 'words.']
for index in range(len(words)):
    words[index] = words[index].upper( )
print(words)
# ['THIS', 'EXAMPLE', 'HAS', '5', 'WORDS.']

# List methods
# The method insert expects an integer index and the new element as arguments
example = [1, 2]
print(example)
# [1, 2]
print(example)
# [1, 10, 2]
example.insert(3, 25)
print(example)
# [1, 10, 2, 25]

# The method append adds the new element to the end of the list
example = [1, 2]
print(example)
[1, 2]
example.append(3)
print(example)
[1, 2, 3]
# • The method extend adds the elements of its list argument to the end of the list
example.extend([11, 12, 13])
print(example)
# [1, 2, 3, 11, 12, 13]
print(example) + [14, 15]
# [1, 2, 3, 11, 12, 13, 14, 15]
print(example)
# [1, 2, 3, 11, 12, 13]

# The method pop is used to remove an element at a given position
print(example)
# [1, 2, 10, 11, 12, 13]
example.pop( ) # Remove the last element
13
print(example)
# [1, 2, 10, 11, 12]
example.pop(0) # Remove the first element
# 1
print(example)
# [2, 10, 11, 12]

# in determines an element's presence or absence
# • But does not return position of element (if found)
# • Use method index to locate an element's position in a list
"""
aList = [34, 45, 67]
target = 45
if target in aList:
    print(aList.index(target))
else:
    print(−1) # • Raises an error when the target element is not found
"""

# When the elements can be related by comparing them <, >, and ==, they can be sorted
# • The method sort mutates a list by arranging its elements in ascending order
example = [4, 2, 10, 8]
print(example)
# [4, 2, 10, 8]
example.sort( )
print(example)
# [2, 4, 8, 10]

# Mutator methods (e.g., insert, append, extend, pop and sort) usually return no
# value of interest to caller
# • Python automatically returns the special value: None
aList = [34, 45, 67]
aList = aList.sort( )
print(aList)
# None
# Should be...
aList = [34, 45, 67]
aList.sort( )
print(aList)

# NB. Aliasing Side Effects
first = [10, 20, 30]
second = first
print(first)
# [10, 20, 30]
print(second)
# [10, 20, 30]
first[1] = 99
print(first)
# [10, 99, 30]
print(second)
# [10, 99, 30]

third = [ ]
for element in first:
    third.append(element)
print(first)
# [10, 99, 30]
print(third)
# [10, 99, 30]
first[1] = 100
print(first)
# [10, 100, 30]
print(third)
# [10, 99, 30]

# Object Identity and Structural Equivalence
"""
Programmers might need to see whether two variables refer to the exact same object or to
different objects
• Example, you might want to determine whether one variable is an alias for another
• The == operator returns True if the variables are aliases for the same object.
• Unfortunately, == also returns True if the contents of two different objects are the same
• The first relation is called object identity
• The second relation is called structural equivalence.
• The == operator has no way of distinguishing between these two types of relations.
"""

# Python's is operator can be used to test for object identity
first = [20, 30, 40]
second = first
third = list(first) # Or first[:]
print(first == second)
# True
print(first == third)
# True
print(first is second)
# True
print(first is third)
# False

# Tuples
# • A tuple resembles a list, but is immutable
# • Indicate by enclosing its elements in ( )
fruits = ("apple", "banana")
print(fruits)
# ('apple', 'banana')
meats = ("fish", "poultry")
print(meats)
# ('fish', 'poultry')
food = meats + fruits
print(food)
# ('fish', 'poultry', 'apple', 'banana')
veggies = ["celery", "beans"]
print(tuple(veggies))
# ('celery', 'beans')