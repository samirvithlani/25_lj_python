mumbai ={"raj","parth","amit","sumit"}
pune = {"jay","amit","kunal","neha"}
goa = {"rajvi","priya","amit","neha","krishna","raj"}


#find user who have attended all 3 events
#find user who is present in mumbai and goa
#find user who is present in pune and goa
#find user who is present in mumbai and goa but not in pune
#find user who is not presnt goa but mummbai and pune both


word = "machinelearning"
#print only uniqie char using comprehesion

ans = {i for i in word}
print(ans)

#word = pythonprogramming #remove vowels

x = {i for i in word if i not in "aeiou"}
print(x)

names = ["Alice", "Bob", "Charlie", "David", "Alex"]

x = {i[0] for i in names}
print(x)
