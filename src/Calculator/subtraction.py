def subtraction(self, b, a):
    if ((type(a) is int) or (type(a) is float)) and ((type(b) is int) or (type(b) is float)):
        self.result = a - b
        return self.result
    else:
        print("Not valid input")