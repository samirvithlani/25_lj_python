colors = ["red","green","yellow","yellow","yellow","pink","white","white","black"]
#unique list

uniqueList = []
duplicate=[]

for i in colors:
    #red ,g,y,y
    if i not in uniqueList:
        uniqueList.append(i) #red
    else:
        duplicate.append(i)    
print(uniqueList)        
print(duplicate)

#find duplicate elements
#["yellow","white"]
#find no of duplicate elements