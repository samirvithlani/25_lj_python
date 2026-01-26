colors = ["red","green","yellow","yellow","pink","white","black"]
#colors = ["red","green","yellow","pink","white","black"]

# name = input("enter color name to delete :")
# if name in colors:
#     colors.remove(name)
# else:
#     print("color not present")    

# print(colors)


for c in colors[:]:
    if c =="yellow":
        colors.remove("yellow")

print(colors)  

