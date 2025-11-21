#if 1 cond get true or false on depedent on we need to check other cond..

age = int(input("Enter Age:"))

if age>18:
    print("You are eligible for voating..")
    if age>21:
        print("you are eligible for marrige:")
    else:
        print("you are not eligible for marrige..`")    
else:
    print("you are not eligible for voating..")    
    
    #17>12 True
    if age>12:
        print("you are eligible for schooling..")
    else:
        print("stay home..")    

