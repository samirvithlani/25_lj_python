name = input("Enter Name : ")
upperName = ""

for i in range(0,len(name)):
    if ord(name[i])>=97 and ord(name[i])<=121:
        upperName = upperName + chr(ord(name[i])-32)
    else:
        upperName = upperName + name[i]
print(upperName)            