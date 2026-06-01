#const is special function which has same name as class name
#in python we can create const useing __init__(self):
#2 type const default const param const
#const will call when we create an object of class
#use of const is to initilize class in memory

class Match:
    
    def __init__(self):
        print("default const of Match class called..")
        self.run= 161
        self.wicket =8

    def getScore(self):
        return self.run,self.wicket

m = Match()        
r,w = m.getScore()
print(r)
print(w)

m2 = Match()
r,w = m.getScore()
print(r)
print(w)
    
    
    