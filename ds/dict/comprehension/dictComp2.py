users =["amit","sumit","raj","parth","jay","sneha","kunal","priyanka","karina"]

#if
userswithlen = {i:len(i) for i in users if len(i)>4}
print(userswithlen)

names= ["naman","ram","shyam","bob","jay","madam"]
#{naman:"palindrome","ram":"not"}

nameswithpalin = {i:"palindrome" if i == i[::-1] else "not palndrome" for i in names}
print(nameswithpalin)

#numbers = [25....] #even odd

#marks = {"Samir": 85, "Rahul": 40, "Aman": 72}
#dict
#result = {"Samir":"pass","Rahul":"Fails"}



#data = {"a": 1, "b": 2, "c": 3}
#data ={1:"a",2:"b",3:"c"}

#data = {"name": "samir", "city": "ahmedabad"}
#{"NAME": "samir", "CITY": "ahmedabad"}

#remove Negative Values
#data = {"a": 10, "b": -5, "c": 20, "d": -2}