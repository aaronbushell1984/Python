def cat_age(years):
    if years <= 0:
        return 0
    
    if years == 1:
        return 15
    elif years == 2:
        return 24
    else:
        return 24 + (years - 2) * 4
