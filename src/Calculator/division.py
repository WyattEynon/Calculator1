def division(self,a,b):
    if ((type(a) is int) or (type(a) is float)):
        try:
            self.result = b / a
            return self.result
        except ZeroDivisionError:
            print("Divide By Zero Error")
            return None
    else:
        print("Not valid input")