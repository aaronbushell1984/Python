# ***LESSON***

languages = ["Python", "Java", "Javascript", "SQL"]

# slicing
print("First element:", languages[0])
print("First element:", languages[-1])
print("Step:", languages[0:3:2])
part_languages = languages[0:3:2]
print("Part:", part_languages)

# membership
if "Java" in languages:
    print("Java is present")
if "c++" in languages:
    print("C++ not present")

# list manipulation
# append and insert
languages.append("c++")
languages.insert(2, "c#")
print("After additions", languages)

# change individual
languages[2] = "C#"

# remove last
languages.pop()

# defend against errors
if "Python" in languages:
    languages.remove("Python")
print("Altered list", languages)

# sort alphabettically or numerically
languages.sort()
print("sorted", languages)

# Reversing
languages.reverse()
print("Reversed", languages)

# Extend another list
# NB EXTEND AND APPEND DO DIFFERENT THINGS - APPENDING A LIST NESTS THE LIST
other_languages = ["Cobol", "Pascal"]
languages.extend(other_languages)
print("Extended languages", languages)

# mixed lists are possible but may cause problems with type
empty_list = []
empty_list.append("Apple")
empty_list.append(0.48)
empty_list.append(12)
empty_list.append(True)
print(empty_list)

# built-in functions
number = [1,2,3,4,5,6,13,4,9]
print(min(number))
# 1
print(max(number))
# 13
print(len(number))
# 9

# equality - NB REFERENCES POINT TO SAME LIST
numbers2 = number
print(number == numbers2)
#true
numbers2.append(99)
print(number == numbers2)
#true
print(number)
# the equality check only checks if contents are the same
numbers3 = [1,2,3,4,5,6,13,4,9]
print(number == numbers3)
#true

# slicing
name = "Bill Bloggs"
print("\nDemo Slicing")
print(name[0]) # zero indexed
print(name[1:4])
print(name[-4])
print(name[-4:])
# using variables
start = 1
end = 5
print(name[start:end])
# Index Example
email = "bill.bloggs@fdmgroup.com"
at_index = email.index("@")
print("index pf @ character =", at_index)
# slice
print("name only part =", email[0:at_index])

# Remove all even numbers from this list
# NB the list must be copied or loop breaks
numbers = [1,2,3,4,5,6,7,88,2]
for number in numbers.copy():
    if number % 2 == 0:
        numbers.remove(number)
print("Odd numbers", numbers)

# Not using max but with a loop and if statements, find and print the largest number
more_numbers = [9,5,7,26,23]
largest = 0
for number in more_numbers:
    if number > largest:
        largest = number

print("Largest =", largest)


# ***SLIDES***

# The Structure of Strings
# A string is a data structure
# Data structure: Consists of smaller pieces of data
# String's length: Number of characters it contains (0+)

# Example:
name = "Alan Turing"
name[0] # Examine the first character
#'A'
name[3] # Examine the fourth character
#'n'
name[len(name)] # Oops! An index error!
#IndexError: string index out of range
name[len(name)-1] # Examine the last character
#'g'
name[-1] # Shorthand for the last character
#'g'
name[-2] # Shorthand for next to last character
#'n'

# Use a count-controlled loop
data = "Hi there!"
for index in range(len(data)):
    print(index, data[index])
"""
0 H
1 i
2
3 t
4 h
5 e
6 r
7 e
8 !
"""
# Slicing for Substrings
myFile = "myfile.txt" # The entire string
myFile[0:]
#'myfile.txt'
myFile[0:1] # The first character
#'m'
myFile[0:2] # The first two characters
#'my'
myFile[:len(myFile)] # The entire string
#'myfile.txt'
#myFile[−3:] # The last three characters
#'txt'
myFile[2:6] # Drill to extract 'file'
#'file'

# Testing for a Substring with the in Operator
fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
for fileName in fileList:
    if ".txt" in fileName:
        print(fileName)
# myfile.txt
# yourfile.txt

# String Methods
sentence = "This sentence has no long words"
listOfWords = sentence.split()
print("There are", len(listOfWords), "words. ")
# There are 6 words.

sumWords = 0
for word in listOfWords:
    sumWords += len(word)
    print("The average word length is", sumWords / len(listOfWords))
# The average word length is 4.5

# Example: extracting a filename's extension
"myfile.txt".split('.')
#['myfile', 'txt']
"myfile.py".split('.')
#['myfile', 'py']
"myfile.html".split('.')
#['myfile', 'html']
# • The subscript [-1] extracts the last element
# • Can be used to write an expression for obtaining the filename's extension, as follows:
"myfile.txt".split('.')[-1]
#'txt'