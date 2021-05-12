# 1. Write a function called greet() that will greet a person by name if their name is input, or everyone if no name is input.
def greet(name):
    """print greeting plus name or Everyone"""
    if name == "":
        return print("Hello and Welcome Everyone")
    else:
        return print("Hello and Welcome", name)

name = input("Please enter a name for a greeting or hit enter to greet everyone: ")
greet(name)

# 2. Write a function called area() to calculate the area of a rectangle. Input parameters will be height and width, and the return value will be height multiplied by width.
def area(height, width):
    return height * width

height = int(input("Please input the rectangle height: "))
width = int(input("Please input the rectangle width: "))

print("Your retangle area is: ", area(height, width))

# 3. Add exception handling to your area() function from Exercise 2 to ensure that height and width are positive whole numbers
def area(height, width):
    if height < 1 or width < 1:
        print("Height and Width must be a positive number")
    else:
        print("Your rectangle area is", height * width)

height = int(input("Please input the rectangle height: "))
width = int(input("Please input the rectangle width: "))

area(height, width)

# 4. Write a function called isLeapYear() to test if a year (input by the user) is a leap year. 
# A year is a leap year if:
# It is divisible by 4 (e.g. 2012, 2016, 2020, 2024 are leap years)
# EXCEPT if it is also divisible by 100 (e.g. 2100, 2200 are not leap years)
# EXCEPT if it is also divisible by 400 (e.g. 2000, 2400, 2800 are leap years)
# Your function should return True for a leap year and False for a non-leap year.
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return print("True")
        elif year % 100 == 0:
            return print("False") 
        else:
            return print("True")
    else:
        return print("False")

year = int(input("Please enter a year: "))

is_leap_year(year)

# 5. Create a function called get_lottery_numbers() that generates 6 unique
# random numbers in the range 1-59.
# You will need to import the random module and make use of the randint() function.
import random

def get_lottery_numbers():
    for number in range(1, 7):
        print(random.randint(1,59))

get_lottery_numbers()
# Store the function in a module called lottery.py
# IN FILE
# 6. Create a new module and import the get_lottery_numbers() function from the lottery module. Give it an alias of gln.
# IN FILE

# Write code to generate and display a set of lottery numbers, using the imported function.
# IN FILE

# 7. Using the shop_data.csv file, write a Pandas program to select and display the rows where Revenue is greater than 700.

# 8. Using the shop_data.csv file, write a Pandas program to select and display the Sales Region and No. sold columns.

# 9. Using the sales_data.csv file, write a Pandas program to select the Sales Region and Direct costs columns and then display the sum of Direct costs, grouped by Sales Region and sorted in ascending order by the Direct costs column.

# 10. Using the shop_data.csv file, create a scatterplot with Matplotlib showing Direct costs plotted against Revenue.

# Display red markers only at the plot points (no lines).

# Add a chart title and axis labels.

# 11. Using the shop_data.csv file, create a bar chart with Matplotlib showing total Revenue grouped by Store-type.

# Display a grid and colour the bars with the hexadecimal colour code of your choice.

# Add a chart title and axis labels.

# 12. Using the shop_data.csv file, create a pie chart with Matplotlib showing No. sold per Sales Region as a percentage of all sales.

# Add a title for the chart.