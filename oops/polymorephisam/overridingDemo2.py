from abc import ABC,abstractmethod
#abc -->pakcage
#ABC class
#abstract base class

#abstract class
class RBI(ABC):
    
    def __init__(self):
        pass
    
    
    @abstractmethod
    def withdraw(self):
        pass
    
    def loan(self):
        pass


class SBI(RBI):
    
    def __init__(self):
        pass
    
    
    def withdraw(self):
        print("withdraw from SBI")

s = SBI()
s.withdraw()        
        
        
                    
        
            