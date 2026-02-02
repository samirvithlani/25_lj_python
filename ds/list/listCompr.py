#range() comprehension

#[1,2,3,4,5]

# data=[]
# for i in range(1,6):
#     data.append(i)


#comprehension version...
data = [i for i in range(1,6)]
print(data)    

#[1,4,9,16,25]
data2 = [i**2 for i in range(1,6)]
print(data2)