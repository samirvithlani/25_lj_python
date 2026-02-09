users = ("ram","shyam","amit","sumit","raj")

x = users.count("shyam")
print(x)

x1 = users.index("amit")
print("index...",x1)


name ="raj"
if name in users:
    ind = users.index(name)
    print("index...",ind)
else:
    print("name not found..")    
