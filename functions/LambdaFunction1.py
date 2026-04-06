x = lambda : print("hello")
x()

x1 = lambda a,b:print("ans",a+b)
x1(100,20)

avg = lambda a,b,c : (a+b+c)/3
x2 = avg(10,20,30)
print(x2)

x3 = lambda fname,lname : fname + " "+lname
fullName = x3("Virat","Kohli")
print(fullName)

#if any funciton is returing any value we can call in side print
print(x3("Ms","Dhoni"))