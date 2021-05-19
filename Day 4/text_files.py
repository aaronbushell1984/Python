# ***LESSON***
import io

def write_text_file(file_name, write_text, write_or_append):
    """open file write_or_append is w or r flag"""
    file = open(file_name, write_or_append)
    file.write(write_text)
    file.close()
    return

def read_text_file(file_name):
    success = False
    file = io.StringIO() # Declared so finally block can see file
    try:   # prevents an error from this example - read_text_file("xyz")
        file = open(file_name)
        text = file.read()
        print(text)
        success = True
    except FileNotFoundError: # error/ exception handling
        print(f"File not found: {file_name}")
    except OSError:
        print(OSError)
    except:
        print("Some other error") # final catch all. #NB EXCEPT MUST BE IN ORDER OF SPECIFICITY
    finally: # always executes
        file.close()
    return success

filename = "todolist.txt"
todo = "1. Go to shops \n2. Exercise \n3. Walk the dog\n"

write_text_file(filename, todo, "a")
read_text_file(filename)

# produces crash
read_text_file("xyz")


# ***SLIDES***

# Data can be written to a text file using a file object
# • To open a file for writing:
f = open("myfile.txt", 'w')
# • If file does not exist, it is created
# • If it already exists, Python opens it; when data are written to the file and the file is closed
# • Any data previously existing in the file are erased

# • This statement writes two lines of text to the file:
f.write("First line.\nSecond line.\n")
# • When all outputs are finished, close the file:
f.close( )

# The file method write expects a string as an argument
# • Other types of data must first be converted to strings before being written to output file
# • For example: using str
# • Code segment that illustrates the output of integers to a text file
import random
f = open("integers.txt", 'w')
for count in range(500):
    number = random.randint(1, 500)
    f  .write(str(number) + '\n')
f.close( )

# Code segment that illustrates appending data to a text file:
import random
f = open("integers.txt", 'a')
for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + '\n')
f.close( )

 # You must close the file after writing or appending to a file. There are a few ways to do this:
# • The first is to use close( )
# • You can also use a try-finally block:
f = open("myfile.txt", 'w')
try:
    f.write("First line.\nSecond line.\n")
finally:
    f.close( )
#• Using the with statement automatically takes care of closing the file:
with open("myfile.txt", 'w') as f:
    f.write("First line.\nSecond line.\n")

# You open a file for input in a manner similar to opening a file for output
f = open("myfile.txt", 'r')
# • If the path name is not accessible from the current working directory, Python raises an error
# • Note: You don’t need to close a file if you just open it for reading
# • There are several ways to read data from a file
# • Example: the read method
text = f.read()
text
'First line.\nSecond line.\n'
print(text)
# First line.
# Second line.

# • After input is finished, read returns an empty string
f = open("myfile.txt", 'r')
for line in f:
    print(line)
# First line.
# Second line.
# • Next code segment inputs lines of text with readline:
f = open("myfile.txt", 'r')
while True:
    line = f.readline()
    if line == "":
        break
    print(line)
# First line.
# Second line.

# Reading Numbers from a File
# In Python, string representations of integers and floating-point numbers can be 
# converted to the numbers by using the functions int and float:
f = open("integers.txt", 'r')
theSum = 0
for line in f:
    line = line.strip()
    number = int(line)
    theSum += number
print("The sum is", theSum)

# The next code segment modifies the previous one to handle integers separated 
# by spaces and/or newlines:
f = open("integers.txt", 'r')
theSum = 0
for line in f:
    wordlist = line.split()
    for word in wordlist:
        number = int(word)
        theSum += number
print("The sum is", theSum)

# Directory navigation in python
childFile = open("child/myfile.txt", 'r')
parentFile = open("../myfile.txt", 'r')
siblingFile = open("../sibling/myfile.txt", 'r')

#  For example, before attempting to open a file for input, you should check to see if file exists
# • Function os.path.exists supports this checking
# Example: To print the names of all files in the current working directory with a .txt extension:
import os
currentDirectoryPath = os.getcwd()
listOfFileNames = os.listdir(currentDirectoryPath)
for name in listOfFileNames:
    if ".txt" in name:
        print(name)
