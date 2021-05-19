# Write a Python function to find the Max of three numbers

def max_three(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        return number1
    if number2 > number1 and number2 > number3:
        return number2
    if number3 > number1 and number3 > number2:
        return number3

number1 = 11
number2 = 1
number3 = 10
print(max_three(number1, number2, number3))