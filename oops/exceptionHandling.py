try:
    no1 = int(input("enter no 1:"))
    no2 = int(input("enter no 2:"))
    ans = no1 / no2 #exception ... except block
    print("ans = ",ans)
    
except ZeroDivisionError:
    print("can not divide by zero..")    
except (ValueError,TypeError) as e:
    print("check input..")    
except:
    print("error..")    
    
    

