def getSum(*args):
    total=0
    for i in args:
        total+=i
    return total     
        

ans = getSum(10,20,30,40,50)
print("ans ",ans)


def checkDt(*args):
    flag = True
    for i in args:
        if type(i)!= int:
            flag  =False
            break
    return flag

ans =checkDt("x",10,20,"abc")        
print(ans)