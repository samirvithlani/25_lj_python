class Emp:
    
    def __init__(self,sal):
        self.sal = sal
        
    def __eq__(self, other):
        return self.sal == other.sal


e1 = Emp(22000)    
e2 = Emp(22000)    

#gt ge lt le eq __add__ __sub__ __truediv__

if e1 == e2:
    print("both havgin same salry")

else:
    print("both having diff salary")    
            