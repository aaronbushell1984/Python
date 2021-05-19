
def sumproduct(list1,list2):
    sum = 0
    numberinlist = len(list1)
    if len(list1) != len(list2):
        return sum
    for i in range(0, numberinlist):
        sum += (list1[i] * list2[i])
    return sum
list1 = [1, 2] 
list2 = [3, 4]
print(sumproduct(list1, list2))
