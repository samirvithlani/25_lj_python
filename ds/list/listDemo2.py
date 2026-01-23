users =["ram","arjun","krishna","sudama","bhim","ram"]

# add 1 element
users.append("sahdev") #it will add at last index..
print(users)

users.insert(3,"yudhisthir") #3  index...
print(users)

tobeadded = ["draupadi","subhdra","kunti"]
users.extend(tobeadded) #extend last..
users.extend(["dhuryodhan"])
print(users)

users.extend("bhishm")
print(users)