data = {"ram","krishna","arjun"}
print(data)


data.add("bhim")
print(data)
#data.update({"seeta","bhim","arjun","lakshman"}) #iterable
#data.update(["seeta","bhim","arjun","lakshman"]) #iterable
data.update(("seeta","bhim","arjun","lakshman")) #iterable
data.update("seeta") #iterable
print(data)