min= None
max =None
same =None

a = int(input("Enter a :"))
b = int(input("Enter b :"))

if a>b:
    max =a
    min = b
elif a == b:
      same = a  
else:
    max = b
    min = a

print("min = ",min)      
print("max = ",max)     
print("same = ",same)      