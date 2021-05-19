def is_perfect(number):
    if number <= 0:
        return False
    divisors_sum = 0
    for int in range(1, number):
        if number % int == 0:
            divisors_sum += int
            print(divisors_sum)
    if divisors_sum == number:
        return True
    else:
        return False

number = -6
print(is_perfect(number))