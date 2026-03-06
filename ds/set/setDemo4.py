data1 = {"ram","seeta","lakshman","kush","luv","krishna"}
data2 = {"ram","arjunn","bhim","sahdeve","krishna","draupadi"}

# print(data1)
# print(data2)

#x  = data1.union(data2)
x = data1 | data2
print(x)

#x = data1.intersection(data2)
x = data1 & data2
print(x)

#x = data1.difference(data2)
x = data2 -data1
print(x)

x = data1.symmetric_difference(data2)
print(x)

y = data1.issuperset(data2)
print(y)

y = data2.issubset(data1)
print(y)

