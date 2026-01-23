marks = [90,87,65,99,79,81]
print(marks)

#marks.pop()
removedElm = marks.pop() #ig empty IndexError: pop from empty list
print("removing....",removedElm)
print(marks)


removedElm = marks.pop(3) #3rd index IndexError: pop index out of range if outside of len...
print("removing....",removedElm)
print(marks)


#remove
marks.remove(87) # error if not present
print("after remove",marks)