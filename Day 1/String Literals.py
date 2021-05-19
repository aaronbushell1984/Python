# ***LESSON***

"""
Multi Line comments can be addeded as doc comments...
between triple quotation marks
"""

# Lesson Example
my_pet = "Dog"
your_pet = "Cat"
print("My pet is a " + my_pet)

# Equality check using == and assigned to variable
are_pets_the_same = (my_pet == your_pet)
print("Do we have the same pets?", are_pets_the_same)

# Print type of variables etc...
print(type(my_pet))
print(type(are_pets_the_same))

# Dot notation to apply built in methods - String specific functions
name = "Bill Bloggs"
print(name.upper())
print(name.count("B"))
#replace
print(name.replace("gg", "*"))
# add in text
print("Does name end with B?", name.endswith("B"))
# assign result to new variable
name_uppercase = name.upper()
print(name_uppercase)

# Dot notation - Integer specific functions
number = 100
print(number.bit_length())

# Index Example
email = "bill.bloggs@fdmgroup.com"
at_index = email.index("@")
print("index of @ character =", at_index)
# slice
print("name only part =", email[0:at_index])

# ***SLIDES***

# In Python, a string literal is a sequence of characters enclosed in single or double quotation marks
print("I'm using a single quote in this string!")

# Use ''' and """ for multi-line paragraphs
print("""This long sentence extends
all the way to the next line.""")

# Concatenation
print("Welcome" + "to" + "FDM!")

# The * operator allows you to build a string by repeating another string a given number of times
print("!" * 10 + "Python")

# N.B convention is capitals for SYMBOLIC_CONSTANTS and lowercase for_variables
