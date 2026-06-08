class Vehicle:
    
    def __init__(self,engine,seat,type):
        print("default const of vehicle class")
        self.engine=engine #v8
        self.seat=seat
        self.type=type


class Car(Vehicle):
    
    def __init__(self,engine,seat,type):
        #parent class const call.
        print("car class const called...")
        super().__init__(engine,seat,type)        
    
    def getVehInfo(self):
        print("Engine = ",self.engine)    
        print("Seats = ",self.seat)
        print("type =",self.type)


c = Car("v8",5,"Sedan")
c.getVehInfo()
c2 = Car("v8",2,"mustang")
c2.getVehInfo()

#p -->user -->name
#c -->employee,manager

#employee name-
#manager -->name        
        
    
            