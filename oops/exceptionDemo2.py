try:
    no1 = int(input("enter no 1:"))
    no2 = int(input("enter no 2:"))
    ans = no1 / no2 #exception ... except block
    print("ans = ",ans)
    
except ZeroDivisionError as e:
    #print("can not divide by zero..")    
    print(e)
except ValueError as e:
    #print("check input..")    
    print(e)
except Exception as e:
    print("error..",e)    

finally:
    print("finally exceute")    
    

