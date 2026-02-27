users =["amit","sumit","raj","parth","jay","sneha","kunal","priyanka","karina"]

#if
userswithlen = {i:len(i) for i in users if len(i)>4}
print(userswithlen)

names= ["naman","ram","shyam","bob","jay","madam"]
#{naman:"palindrome","ram":"not"}

nameswithpalin = {i:"palindrome" if i == i[::-1] else "not palndrome" for i in names}
print(nameswithpalin)

#numbers = [25....] #even odd