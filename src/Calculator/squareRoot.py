def squareRoot(self, a):
    if ((type(a) is int) or (type(a) is float)):
        self.result = a ** 0.5
        return self.result
    else:
        print("Not valid input")