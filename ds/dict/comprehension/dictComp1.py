#{1:1,2:2,3:3,4:4:5:5}

data ={}

for i in range(1,6):
    data[i]=i

print(data)    

#compre

data = {i:i for i in range(1,6)}
print(data)

#{1:1,2:4,3:9,4:16,5:25}
data1 = {i:i**2 for i in range(1,6)}
print(data1)
