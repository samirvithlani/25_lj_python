

def admission():
    pass


admission("raj",age=19,course="IT") #valid
admission("parth",age=16,course="CS") #not valid age <18
admission("jay",course="IT") #not valid age is not present
admission("amit") #not valid both age and course not present
admission("kunal",age=22) #not valid course not present