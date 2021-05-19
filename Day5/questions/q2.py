def cat_age(catage):
    if catage <= 0:
        return 0
    elif catage == 1:
        return 15
    elif catage == 2:
        return 24
    else:
        return 24 + ((catage-2) * 4)