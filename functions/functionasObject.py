def test():
    print("test function called..")
    return 100

# x = test()    
# print("x",x)

x = test  
print("x",x)
x()

def sum(a,b,c):
    return a + b + c


y = sum
print(y)
ans = y(10,20,30)
print(ans)

