class Game:
    
    def __init__(self,points):
        self.points = points
    
    def __sub__(self, other):
        return Game(other.points-self.points)    


lev1 =Game(100)    
lev2 = Game(250)

final = lev1 - lev2
print(final.points)
