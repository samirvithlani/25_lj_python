users =["amit","sumit","raj","parth","jay","sneha","kunal"]

#userwithlen ={}

# for i in users:
#     userwithlen[i]=len(i)

#compre

userwithlen ={i:len(i) for i in users}
print(userwithlen)    

userwithinitial = {i[0]:i for i in users}
print(userwithinitial)