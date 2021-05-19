def factorial(number):
    if number == 0:
        return 1
    else:
        total = 1
        for count in range(number, 0, -1):
            total *= count
        return total

#### NB return n * factorial(n-1)
