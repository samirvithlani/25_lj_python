
def check(func):
    def inner(name,**kwargs):
        if "age" not in kwargs:
            print("age is not present")
            return
        if "course" not in kwargs:
            print("course is not present")
            return
        if kwargs['age'] < 18:
            print("not valid...")
            return 
        
        func(name,**kwargs)     
    return inner    
            
                
    

@check
def admission(name,**kwargs):
    print("admisison granted..")


admission("raj",age=19,course="IT") #valid
admission("parth",age=16,course="CS") #not valid age <18
admission("jay",course="IT") #not valid age is not present
admission("amit") #not valid both age and course not present
admission("kunal",age=22) #not valid course not present