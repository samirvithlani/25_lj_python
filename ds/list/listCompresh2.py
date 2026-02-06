users = ["ram","shyam","amit","sumit","geeta","jaya","rama"]

# filrUsers =[]

# for i in users:
#     if len(i)>4:
#         filrUsers.append(i)
#print(filrUsers)        

filtUsers = [i for i in users if len(i)>4]
print(filtUsers)


users = ["ram","shyam","amit","sumit","naman","geeta","jaya","rama","bob"]
#label =["no",nom=,no....]

filtUsers2 = ["yes" if i == i[::-1] else "No" for i in users]
print(filtUsers2)

numbers = [-100,100,0,20,0,-90,98,97,67,-32]
numberLab = ["pos" if i>0 else "NEG" for i in numbers]
print(numberLab)
numberLab2 = ["pos" if i>0 else ("ZERO" if i ==0 else "NEG") for i in numbers]
print(numberLab2)


sales= [100,20,45,67,89,120,89,78]
sales50 =[i for i in sales if i>50]
print(sales50)
evenoddsalses = ["even" if i %2 ==0 else "odd" for i in sales]
#evenoddsalses = ["even" if i %2 ==0 else "odd" for i in sales if i>50]
print(evenoddsalses)
