marks = [10,20,23,12,14,12]
print(marks)

ind = marks.index(12)
print("index ",ind)


cnt =marks.count(12)
print("cnt",cnt)

#sort...
#marks.sort() #asc
#marks.sort(reverse=True) #asc
marks.reverse()
print(marks)