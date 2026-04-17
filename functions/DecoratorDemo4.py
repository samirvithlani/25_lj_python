def loginRequired(func):
    def inner(*args,role):
        if role in args:
            print("authorized access:")
            func(args,role=role)
        else:
            print("unauthorized access:")    
    return inner


@loginRequired
def accessHomePage(*args,role):
    print("accessing home page by",role)
accessHomePage("admin","manager","user",role="abcd")    


@loginRequired
def accessCartPage(*args,role):
    print("accesing cart by",role)


accessCartPage("user","admin",role="user")    
