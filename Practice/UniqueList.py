def unique_list(list):
    unique = []
    for item in list:
        if item not in unique:
            unique.append(item)
    return unique

list = [1,2,3,3,3,3,4,5]
print(unique_list(list))