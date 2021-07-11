def randomSeed(self,a,b,s):
    import random
    random.seed(s)
    self.result = random.randint(a,b)
    return self.result