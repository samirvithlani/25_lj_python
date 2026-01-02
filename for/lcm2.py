a = int(input("Enter a: "))
b = int(input("Enter b: "))
i = 1
#1<150
while(i<=a*b):
    if(i%a==0 and i%b==0):
        print(i, " is lcm")
        break