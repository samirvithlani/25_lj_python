# def outer():
#     print("outer called...")
    
#     def inner():
#         print("inner called..")

#     inner()

# outer()        

# def outer(a):
#     print("outer called...",a)
    
#     def inner(x,y):
#         print("inner called..",a)
#         print(x,y)

#     #print("outer x y",x,y)
#     inner(10,20)

# outer(12)        


def outer(a):
    print("outer called...",a)
    
    def inner(x,y):
        print("inner called..",a)
        print(x,y)
        return x+y

    #print("outer x y",x,y)
    sum = inner(10,20)
    print("sum from inner",sum)
    return a**2

sq = outer(12)        
print("sq =",sq)
