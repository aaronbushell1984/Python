def prime(number:int):
    if number <= 0:
        return False
    for factor in range(number-1, 1, -1):
        if number % factor == 0:
            return False
    return True