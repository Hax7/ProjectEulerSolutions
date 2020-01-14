def fiboEvenSum(limit):
    previousFibNum = currentFibNum = 1
    nextFibNum = 0
    sumOfEvenFibNum = 0
    while nextFibNum < limit:
        nextFibNum = previousFibNum + currentFibNum
        previousFibNum = currentFibNum
        currentFibNum = nextFibNum
        if previousFibNum % 2 == 0:
            sumOfEvenFibNum += previousFibNum
    return sumOfEvenFibNum
