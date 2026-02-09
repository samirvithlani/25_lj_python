users = ("ram","shyam","amit","sumit","raj")
print(users)

userList = list(users)
print(userList)
userList.append("ajay")

users = tuple(userList) #error???
print(users)