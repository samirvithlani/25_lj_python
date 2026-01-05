name = input("Enter Name : ")
upperName = ""

for i in name:  
    
    if ord(i)>=97 and ord(i)<=121:
        upperName = upperName +  chr(ord(i)-32)
    else:
        
        upperName = upperName +i        

print(upperName)    