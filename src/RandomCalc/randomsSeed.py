def randomsSeed(self,a,b,n,s):
    import random
    random.seed(s)
    self.result = random.randint(a,b,n)
    return self.result