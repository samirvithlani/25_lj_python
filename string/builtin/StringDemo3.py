#boolean

data = ""

flag = data.startswith("j")
print(flag)
print('endswith',data.endswith("a"))
print("isalnum",data.isalnum())
print("alpha...",data.isalpha())
print("numric..",data.isnumeric())
#print(data.isdigit())
print("lower",data.islower()) #"abcd" #"abcd1" # "abc " # "Abc"
print("upper",data.isupper())
print("isspace",data.isspace()) #" "
print("is title",data.istitle()) #
print(data.isprintable()) # \n 

