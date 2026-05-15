users = ["amit","sumit","raj","parth"]
marks = [23,23,24,21,19]
age = [19,20,19,18,17]


for i,j,k in zip(users,marks,age):
    print(i,"-",j,"-",k)


#enumrate:

users = ["amit","sumit","raj","parth"]
# for i in range(0,len(users)):
#     print("i",i,users[i])


# for i in users:
#     print(i)    

for index,elm in enumerate(users):
    print("inddex",index,"value",elm)
    

#all any
#js -->every some
marks = [23,23,24,21,19]
#if all subject marks >20 pass :fail
# flag = True
# for i in marks:
#     if i<20:
#         flag=False
#         break

# print(flag)    
    
flag = all(m>15 for m in marks)
print(flag)

flag1 = any(m>25 for m in marks)
print(flag1)

students = {"amit":23,"summit":24,"raj":23,"ajay":24,"sujay":23}
#bonus = False  >24 [1] #all
#flag = False  > 20[] #any

#sorted
nums = [5,2,1,8]
#sortlist =sorted(nums)
sortlist =sorted(nums,reverse=True)
print(sortlist)


users = ["amit","sumit","raj","parth"]
#sortedUsers = sorted(users)
#sortedUsers = sorted(users,reverse=True)
sortedUsers = sorted(users,key=len)

print(sortedUsers)

nums = [5,2,-1,8,-20]
sortlist =sorted(nums)
print(sortlist)

#ignore signes
#abs
x = 100
print(x)
y = -100
print(y)
print(abs(y))

#sort ignoring sign
result = sorted(nums,key= lambda x:abs(x))
print(result)

#tuple
students = [("harsh",80),("raj",81),("parth",77)]
#result = sorted(students) #[0]
#result = sorted(students,key=lambda x:x[1]) #[0]
result = sorted(students,key=lambda x:x[1],reverse=True) #[0]
print(result)
    
 
#sort.   
#students = {"amit":23,"summit":24,"raj":23,"ajay":24,"sujay":23}    