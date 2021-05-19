def binary_odds(binary):
    oddlist = []
    listbinary = list(binary.split(" "))
    if binary == "":
        return oddlist
    else:
        for i in range(0, len(listbinary)):
            listbinary[i] = int(listbinary[i])
        for num in listbinary:
            if num % 2 != 0:
                oddlist.append(num)
        for i in range(0, len(oddlist)):
            oddlist[i] = str(oddlist[i])
        return oddlist


