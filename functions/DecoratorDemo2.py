# def smartdiv(func): #func == div
#     def inner(x,y):
#         print("no1 inside inner",x)
#         print("no2 inside inner",y)
#         print("smart div called...")
#         func(x,y) # div
#     return inner

    

# @smartdiv
# def div(no1,no2):
#     print("div...",no1/no2)

# div(10,2)    



def smartdiv(func): #func == div
    def inner(x,y):
        print("no1 inside inner",x)
        print("no2 inside inner",y)
        print("smart div called...")
        #func(x,y) # div
        if y==0:
            print("can not divide by zero")
        else:
            func(x,y)    
    return inner

    

@smartdiv
def div(no1,no2):
    print("div...",no1/no2)

#div(10,2)    
div(10,0)