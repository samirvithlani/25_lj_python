class Father:
    
    city = "dubai"
    veh = "car" 
    
    def __init__(self):
        print("father class const called..")
        self.amount = 20000
        self.a = 1000


class Mother:
    
    city = "tokio"
    veh = "cycle" 
    def __init__(self):
        print("mother class const called..")        
        self.amount = 10000
        self.b =200


class Child(Mother,Father):
    
    def __init__(self):
        super().__init__()
    
    def getINfo(self):
        print("amount = ",self.amount)
        print("city = ",self.city)
        print("veh = ",self.veh)
        #print("a = ",self.a)
        print("b = ",self.b)
        print("city fath",Father.city)
        print("city fath",Father.veh)



c =Child()        
c.getINfo()
            