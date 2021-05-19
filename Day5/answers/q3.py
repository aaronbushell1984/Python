def sumproduct(list1,list2):
    sum = 0
    
    if len(list1) != len(list2):
        return sum
    else:
        for index in range(len(list1)):
            sum += (list1[index] * list2[index])
    
    return sum
