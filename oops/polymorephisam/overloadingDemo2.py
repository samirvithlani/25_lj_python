
from multipledispatch import dispatch

class Bank:
    
    def __init__(self):
        print("bank class const called...")
    
    @dispatch(int,int)
    def deposit(self,a,b):
        print("deposit with double argument called..",a,b)        
        
    @dispatch(int)    
    def deposit(self,a):
        print("deposit with single argument called..",a)    


b = Bank()
b.deposit(10,20)        