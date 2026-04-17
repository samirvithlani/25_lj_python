

def loginRequired(func):
    def inner(role):
        if role =="ADMIN":
            func(role)
        else:
            print("unauthorized")    
    return inner        



@loginRequired
def access_data(role):
    print("accessing data and my role is",role)

access_data("ADMIN")    

@loginRequired
def access_files(role):
    print("accessing files",role)
    
#access_files("manager")    
access_files('ADMIN')