def squaring(self, a):
    if ((type(a) is int) or (type(a) is float)):
        self.result = a * a
        return self.result
    else:
        print("Not valid input")