data = "hi thIs is india"
#find no of space..
space = 0

# for i in data:
#     if i ==" ":
#         space+=1


for i in range(0,len(data)):
    if data[i]==" ":
        space+=1

print(f"space = {space+1}")        

#no of vowels A E I O U

vowels =0
for i in data:
    #In membership
    if i in "aeiouAEIOU":
        vowels+=1

print("vowels count...",vowels)        

