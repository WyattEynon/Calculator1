from Calculator.Division import division
from Calculator.Addition import addition

def mean(data):
    dataLength = len(data)
    dataSum = 0
    for x in data:
        total = addition(dataSum, x)
    return division(dataLength, dataSum)