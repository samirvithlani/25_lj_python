class Bank:
    
    def __init__(self):
        print("bank class const called...")
    
    def deposit(self,a,b):
        print("deposit with double argument called..",a,b)        
        
    def deposit(self,a):
        print("deposit with single argument called..",a)    


b = Bank()
b.deposit(10)        