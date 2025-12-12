#123 ->
no = 1235
count=0

# no = no // 10 #123 / 10 - 12 no =12
# count+=1  #1

# no = no //10 #12//10 = 1
# count+=1 #2

# no = no //10 #1//10 = 0
# count+=1 #3

while(no>0):
    no = no //10
    count+=1

#-------------------#
print(count)