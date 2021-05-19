def multiply(list):
    product = 1
    for number in list:
        product *= number
    return product

list = [8, 2, 3, -1, 7]
print(multiply(list))