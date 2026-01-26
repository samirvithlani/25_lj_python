colors = ["red","green","yellow","yellow","pink","white","white","black"]
#unique list

uniqueList = []

for i in colors:
    #red ,g,y,y
    if i not in uniqueList:
        uniqueList.append(i) #red
print(uniqueList)        

#find duplicate elements
#["yellow","white"]
#find no of duplicate elements