x = lambda x: "even" if x %2==0 else "odd"
print(x(200))

x1 = lambda name:"palindrome" if name == name[::-1] else "Not"
print(x1("naman"))

findMax = lambda no1,no2 : no1 if no1 > no2 else no2
print(findMax(100,200))

