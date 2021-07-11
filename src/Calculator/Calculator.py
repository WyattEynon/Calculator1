from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.squaring import squaring
from Calculator.squareRoot import squareRoot
from Calculator.multiplication import multiplication
from Calculator.division import division

class Calculator:

    def __init__(self):
        pass
    result = 0
    #Input Regualtion
    #Operations Below


    def add(self, a, b):
        addition(a,b)
    def subtract(self, b, a):
        subtraction(b,a)
    def square(self, a):
        squaring(a)
    def sqrt(self, a):
        squareRoot(a)
    def multiply(self, a, b):
        multiplication(a,b)
    def divide(self, a, b):
        division(a,b)
