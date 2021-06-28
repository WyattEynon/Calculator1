class Calculator:

    result = 0

    def __init__(self):
        pass
    def add(self, a, b):
        self.result = a + b
        return self.result
    def subtract(self, a, b):
        self.result = a-b
        return self.result
    def square(self, a):
        self.result = a*a
        return self.result
    def sqrt(self, a):
        self.result = a ** 0.5
        return self.result