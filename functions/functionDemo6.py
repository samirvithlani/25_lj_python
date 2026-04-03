#kwrags is not keyword
def getUserData(x,**kwargs):
    print("kwargs",kwargs)
    print("x",x)

#getUserData(name="amit",age=23,salary=34000,x=1000)    
getUserData(1000,name="amit",age=23,salary=34000)    


def getData(*args,**kwargs):
    print("args",args)
    print("kwargs",kwargs)    

getData(10,20,30,x=100,y=200)  


def checkData(**kwargs):
    for i in kwargs.values():
        # if type(i)!= str:
        #     return False
        if not isinstance(i,str):
            return False
    return True

