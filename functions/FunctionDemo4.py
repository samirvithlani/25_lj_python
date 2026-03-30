# def users(x):
#     print(x)

# users("ram","shyam")     #TypeError: users() takes 1 positional argument but 2 were given


#args is not keyword
#def users(*names):valid...
def users(*args):
    print(args)

users("ram","shyam",["ok"])  
users()  
users("ram",22,("ok",))


# def students(*names,x):
#     print(names)
#     print(x)

#1st solution
# def students(x,*names):
#     print("names..",names)
#     print("x =",x)


# students("amit","sumit","jay")    

#2nd solution
def students(*names,x):
    print("names..",names)
    print("x =",x)


students("amit","sumit",x="jay")    
