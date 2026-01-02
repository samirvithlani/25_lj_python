a = 10
b = 15

#30

#find max no from 2
max = 0

# if a>b:
#     max = a
# else:
#     max = b

#Max = 15
lcm =0

while True:
    #  15 % 10 and 15 %15 ==0 FALSE
    # 16 % 10 and 16 % 15 ==0 FALSE
    #.. 20% 10 == 0 and 15 % 20 = FALSE
    #30%10 ==0 and 30 %15 ==0 TRUE
    if max % a ==0 and max % b ==0:
        lcm = max
        break
    max+=1 #16,17,18,19,20,21,22,23,24,25,26,27,28,29,30

print(lcm)                