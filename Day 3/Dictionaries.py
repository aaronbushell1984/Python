# ***LESSONS***
# key/value pairs, key must be unique, mutable
countries = {
    "Brazil"    :   "Coffee",
    "Canada"    :   "Timber",
    "UK"        :   "Services",
}

for key in countries:
    print("key", key)
    print("value", countries[key])

# NB.COMBINED ACCESS OF KEY AND VALUE
for key, value in countries.items():
    print("key:", key, "value:", value)

# Change a value
countries["Canada"] = "Maple Syrup"
print(countries)
# NB TYPO WOULD ADD A NEW KEY WITH NO ERROR
countries["Canadax"] = "Maple Syrup"
print(countries)
# add a new set
countries["France"] = "Wine"
print(countries)
# remove a set
countries.pop("Canadax")
print(countries)

# List inside a dictionary
# Bank account - build up rather than assign immediately
# Create empty
bank = {}
# Create account as lists
davids_account = ["David", 2000.00]
bills_account = ["BILL", 2403.45]
# assign keys to accounts
bank[10000001] = davids_account
bank[10000002] = bills_account
print("\n*** BANK ACCOUNTS ***")
print(bank)
# Access list within a dictionary
bank[10000001][1] += 1000
bank[10000002][0] = "Bill"
print(bank)

# ***SLIDES***

"""
A dictionary organizes information by association, not position
Example:
• When you use a dictionary to look up the definition of "mammal," you don't start at page 1; 
instead, you turn to the words beginning with "M"
• Data structures organized by association are also called tables or association lists
• In Python, a dictionary associates a set of keys with data values
"""

# Examples:
a_phone_book = {'William':'07505455555', 'Stephen':'08705455555'}
personal_information = {'Name':'William'
, 'Age':55}
an_empty_dictionary = { }

# Example:
info = { }
info["name"] = "William"
info["occupation"] = "Developer"
info
{'name':'William', 'occupation':'Developer'}
# • Use [ ] also to replace a value at an existing key:
info["occupation"] = "Manager"
info
{'name':'William', 'occupation':'Manager'}

# Use [ ] to obtain the value associated with a key
# • If key is not present in dictionary, an error is raised
info["name"]
'William'
info["job"]
# Traceback (most recent call last):
#File "<pyshell>", line 1, in <module>
#info["job"]
#Key Error: 'job'

# • If the existence of a key is uncertain, test for it using the operator in
if "job" in info:
    print(info["job"])
# • Easier strategy is to use the method get
print(info.get("job", None))
# None
print(info.get("occupation", None))
# Manager

# To delete an entry from a dictionary, remove its key using the method pop
# • pop expects a key and an optional default value as arguments
print(info.pop("job", None))
# None
print(info.pop("occupation"))
# Manager
print(info)
# {'name':'William'}

# Traversing a Dictionary
# To print all of the keys and their values:
for key in info:
    print(key, info[key])
# • Alternative: Use the dictionary method items( )
grades = {90:'A', 80:'B', 70:'C'}
list(grades.items( ))
# [(90, 'A'), (80,'B'), (70,'C')]
# • Entries are represented as tuples within the list
for (key, value) in grades.items( ):
    print(key, value)

# Sorting a list before traversing the list
info = {"occupation":"Manager","name":"William"}
theKeys = list(info.keys( ))
theKeys.sort( )
for key in theKeys:
    print(key, info[key])

#You can keep a hex-to-binary dictionary as a lookup table to aid in the conversion process
hexToBinaryTable = {
'0':'0000', '1':'0001', '2':'0010',
'3':'0011', '4':'0100', '5':'0101',
'6':'0110', '7':'0111', '8':'1000',
'9':'1001', 'A':'1010', 'B':'1011',
'C':'1100', 'D':'1101', 'E':'1110',
'F':'1111'}

def convert(number, table):
# Builds and returns the base two representation of number.
    binary =   ""
    for digit in number:
        binary = table[digit] + binary
    return binary
print(convert("35A", hexToBinaryTable))
# '001101011010'

# The following script inputs a list of words from a text file and prints their mode
fileName = input("Enter the filename:")
f = open(fileName, 'r')
# Read the text, convert the words to uppercase, & add the words to a list
words = [ ]
for line in f:
    for word in line.split( ):
        words.append(word.upper( ))

# Obtain set of unique words and their frequencies, saving associations in a dictionary
theDictionary = {}
for word in words:
    number = theDictionary.get(word, None)
    if number == None:
# word entered for the first time
        theDictionary[word] = 1
    else:
# word already seen, increment its number
        theDictionary[word] = number + 1
# Find the mode by obtaining the maximum value in the dictionary & determining its key
theMaximum = max(theDictionary.values())
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print("The mode is", key)
        break