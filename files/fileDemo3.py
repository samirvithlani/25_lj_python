#file read..

# file = open("task.txt","r")
# x = file.read()
# print(x)

# with open("task.txt","r") as file:
#     # x =file.readline()
#     # print(x)
    
#     while True:
#         x = file.readline()
#         print(x,end="")
#         if not x:
#             break


# with open("task.txt","r") as file:
#     x = file.readlines() #[]
#     print(x)
#     for i in x:
#         print(i,end="")


with open("task.txt","r") as file:
    for i in file.readlines(): #[]
        print(i,end="")
    