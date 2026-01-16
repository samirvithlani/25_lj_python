#range(sp,ep,step)
#string support neg indexing..

data="java"
print(data)
print(data[0]," - ",data[-4])
print(data[1]," - ",data[-3])
print(data[2]," - ",data[-2])
print(data[3]," -- ",data[-1])

#simple slicing...
text = "PythonProgramming"
print(text[0:6]) #0,1,2,3,4,5

#skip start
print(text[:6]) #0,1,2,3,4,5

#skip end
print(text[1:]) #1,2,3,4,.....len

#fullstring...
print(text[:])
x = text[:]
print(x)


#neg index

print(text[:-6]) #0_____________________ -6-5-4-3-2-1
print(text[-13:-6]) #-13,-12,-11,10,-9,-8,-7,-6


#step param
text = "abcdef"
print(text[::2]) #0 1 2 3 4 5......... increment 2
#ace
print(text[::3]) 

print(text[::-1])
