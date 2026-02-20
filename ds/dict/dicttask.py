data = {101:"raj",102:"parth",103:"jay"}
#x = data.pop(1011,101) pop(key,defaultvalue) #if keuy not found it will not throw error it will return default value
# x = data.pop(1011,"abcd")
# print(x)
# print(data)

while data:
    removedElm = data.popitem()
    print(removedElm[0],"-",removedElm[1])
print(data)    
    