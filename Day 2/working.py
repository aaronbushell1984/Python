total = 0
x = number = int(input("Please enter a number:"))
y = number = int(input("Please enter a number:"))
operator = input("Please enter and arithmetic operator")
while operator:
    if operator == "+":
        total = x + y
    elif operator == "-":
        total = x - y
        break
print(total)