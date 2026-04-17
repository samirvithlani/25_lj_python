#decorators are pure python function which is use for change function behaviour withiut
#change of code
#deco.. are expecting func as argument, and decor.. will return inner function object
#deco will use @above function

def order_food(func): #3
    print(func) #4 func ==throw_party
    def inner(): #7
        print("ordering food..") #8
        func() #9 throw_party()
    return inner  #5  



@order_food #2 #6[control]
def throw_party(): #10
    print("throw party function called...") #11


throw_party()  #1  