def range_check(number, lower, upper):

    if lower >= upper:
        return "Upper must be higher than lower"

    if number in range(lower, upper+1):
        return True
    else:
        return False