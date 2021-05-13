def rightAngledTriangle(length1, length2, length3):
    if length1 < 1 or length2 < 1 or length3 < 1:
        return False
    elif (length1 ** 2)+(length2 ** 2) == (length3 ** 2) or (length2 ** 2)+(length3 ** 2) == (length1 ** 2) or (length1 ** 2)+(length3 ** 2) == (length2 ** 2):
        return True
    else:
        return False