#single line code...
users = ["ram","shyam","amit","sumit","jaya","divya"]

#upperCase -->
#uppersUser=[]

upperUser =[]
for i in users:
    upperUser.append(i.upper())

print(upperUser)    


#comprehension version...

upperUser1 = [i.upper() for i in users]
#[return[append]i for i in users]
print(upperUser1)

users = ["ram","shyam","amit","sumit","jaya","divya"]
#[r,s,a,s,j,d]

usersInitial = []
for i in users:
    usersInitial.append(i[0])

print(usersInitial)    

#comprehension version...
usersInitial1 = [i[0] for i in users]
print(usersInitial1)


#numric
sales = [100,200,300,400,500,600,700] 
#10...
#sales1 = [110,210]
sales1 =[]

for i in sales:
    sales1.append(i+10)

print(sales1)   

#comprehension version...
sales2 =[i+10 for i in sales] 
print(sales2)

#%10% profit

profitSales = [int(i*1.1) for i in sales]
print(profitSales)