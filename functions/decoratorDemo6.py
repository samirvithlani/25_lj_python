def check(func):
    def inner(name,**kwargs):
        if len(kwargs)<3:
            print("not all marks given")
            return
        else:
            func(name,**kwargs)
    return inner        
                
            

@check
def grade(name,**kwargs):
    print("grade..")

grade("amit",maths=80,science=90,english=70) #grade 
grade("amit",maths=80) #grade

