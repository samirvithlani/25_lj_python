class Match:
    
    def __init__(self,r,w):
        self.r = r
        self.w = w
    
    def getScore(self):
        return self.r,self.w

m1 = Match(161,8)    
print("m1 score..",m1.getScore())

m2 = Match(49,10)    
print("m2 score..",m2.getScore())
        