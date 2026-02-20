data = {101:"raj",102:"parth",103:"jay"}
print(data.get(102))
print(data[102])
print(data)
#remove..
if 101 in data:
    removedValue = data.pop(101) #101-raj
    print("removing...",removedValue)
else:
    print("not availlable to remove...")    

print(data)