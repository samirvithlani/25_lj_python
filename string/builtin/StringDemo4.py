data = "java"
ind = data.index("a") #ValueError: substring not found
print("index -> ",ind)

f = data.find("x") # -1
print(f)


email = "google@samir.com"

ind = email.index("o",2) #bodundry
#ind = email.find("o",2) #bodundry
print(ind)
