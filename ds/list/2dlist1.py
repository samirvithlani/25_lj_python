data =[[1,2,3],[4,5,6],[7,8,9]] #3*3
#3 rows 3 columns

# print(data[0])
# print(data[1])
# print(data[2])

# for i in range(0,len(data)):
#     print(data[i])

# print(data[0][0])
# print(data[0][1])
# print(data[2][0])

for i in range(0,len(data)):
    #i=0,i=1,i=2
    for j in range(0,len(data[i])):
        #j=0,j=1
        #data[0][0] =1
        #data[0][1] =2
        #data[0][2] =3
        #data[1][0]=4
        #....
        #data[2][0]
        print(data[i][j],end=" ")
    print()    



#foreach memb....

for i in data:
    for j in i:
        print(j,end=" ")  
    print()        