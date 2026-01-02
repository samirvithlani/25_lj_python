no = int(input("enter no :"))
rem=0
sum=0
temp = no
temp2= no
digits =0

while temp>0:
    temp = temp //10
    digits+=1

print("no of digits = ",digits)  

while temp2>0:
    rem  = temp2 % 10
    #sum  = sum + rem**3
    sum = sum + (rem**digits)
    temp2= temp2 //10

if sum == no:
    print("armstorng")    
else:
    print("not armstrong")    
       