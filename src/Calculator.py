class Calculator:

    def __init__(self):
        pass
    result = 0
    #Input Regualtion
    #Operations Below


    def add(self, a, b):
        if ((type(a) is int) or (type(a) is float)) and ((type(b) is int) or (type(b) is float)):
            self.result = a + b
            return self.result
        else:
            print("Not valid input")
    def subtract(self, b, a):
        if ((type(a) is int) or (type(a) is float)) and ((type(b) is int) or (type(b) is float)):
            self.result = a-b
            return self.result
        else:
            print("Not valid input")
    def square(self, a):
        if ((type(a) is int) or (type(a) is float)) and ((type(b) is int) or (type(b) is float)):
            self.result = a*a
            return self.result
        else:
            print("Not valid input")
    def sqrt(self, a):
        if ((type(a) is int) or (type(a) is float)):
            self.result = a ** 0.5
            return self.result
        else:
            print("Not valid input")
    def multiply(self, a, b):
        if ((type(a) is int) or (type(a) is float)):
            self.result =a * b
            return self.result
        else:
            print("Not valid input")
    def divide(self, a, b):
        if ((type(a) is int) or (type(a) is float)):
            try:
                self.result = b / a
                return self.result
            except ZeroDivisionError:
                print("Divide By Zero Error")
                return None
        else:
            print("Not valid input")
