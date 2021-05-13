def calculateFactorial(N):
    factorialN = 1
    if N == 0:
        factorialN = 1
        return factorialN
    else:
        for number in range(1, N+1):
            factorialN = factorialN * number
        return factorialN
