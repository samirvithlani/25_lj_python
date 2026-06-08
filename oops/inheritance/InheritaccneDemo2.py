class User:
    
    def __init__(self,name):
        print("parent const")
        self.name = name

class Employee(User):
    
    def mark_Att(self):
        print("atte..",self.name)        

class Manager(User):
    def mark_Att(self):
        print("atte..manager",self.name)        



e = Employee("Raj")        
e.mark_Att()
m = Manager("jay")
m.mark_Att()
    
            