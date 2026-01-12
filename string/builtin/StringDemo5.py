data ="javascaript"
#data = data.replace("a","A")
data = data.replace("a","#",4) #count..
print(data)

data1 = "java script is java"
replacedata = ""

for i in range(len(data1)):
    #i=2
    if i >=2 and data1[i]=="a":
            replacedata+="A"
    else:    
        replacedata+=data1[i]        

print(replacedata)            
        