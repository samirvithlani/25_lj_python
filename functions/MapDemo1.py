#map --> interbale object manupplate:
users = ["ram","shyam","amit","krishna","radha"]
user2=[]
for i in users:
    user2.append(i.upper())
print(user2)

users3 = [i.upper() for i in users]
print(users3)

#map
#map(function,object)
users4 = map(lambda x:x.upper(),users)
print(list(users4))

#sales --> 30% disount..
#map will return all data anyhow

userwithcond = list(map(lambda x:len(x)>4,users))
print(userwithcond)

#filter

userwithlen = filter(lambda i:len(i)>4,users)
print(list(userwithlen))

names =["amit","neha","smruti","priya","ajna","amita","mayavati","sushila","radha","jay"]
#nam ends with a store in upper 

names1 = map(lambda x:x.upper(),filter(lambda x:x.endswith("a"),names))
print(list(names1))

#name i -->return -->upper

names2 = map(lambda x:x.upper(),filter(lambda x: "i" in x,names))
print(list(names2))