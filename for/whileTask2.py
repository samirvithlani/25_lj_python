no = int(input("enter no :"))
#123 --> 1 + 2 + 3 = 6 
#123 // 10 -->rem 
#123 % 10 = 3
#123 -->12 --> 123 // 10 = 12
#12 % 10 = 2
#12 --1
#12 // 10 = 1
#1 % 10 =1
sum = 0 #0
#123!=0 True
#12!=0 True
#1!=0 True
#0!=0 False
while no!=0:
    #rem = 123 % 10 = 3
    #rem = 12 % 10 = 2
    #rem = 1 % 10 = 1
    rem = no % 10 
    #sum = 0+ 3 = 3
    #sum = 3 + 2 = 5
    #sum = 5 + 1 = 6
    sum = sum + rem
    #no = 123 // 10 = 12
    #no  = 12 // 10 = 1
    #no = 1 //10 =0
    no = no //10

print("sum = ",sum)    
    