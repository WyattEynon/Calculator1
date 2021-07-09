def multiplication(self, a, b):
    if ((type(a) is int) or (type(a) is float)):
        self.result = a * b
        return self.result
    else:
        print("Not valid input")