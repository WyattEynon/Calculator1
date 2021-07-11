from Calculator import Calculator
from Statistics.Mean import mean

class statistics(Calculator):
    #data=[]

    def mean(self, data):
        self.result=mean(data)
        return self.result

