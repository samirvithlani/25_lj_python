#fileobject = open("location | path ","mode")

#if file present at given path it will overwrite
#if file is not present at given path it will create and write data


# file  = open("demo1.txt","w")
# file.write("\nHi this is 1st line from python")
# file.close()

name = "Fenil"
# file  = open("demo1.txt","w")
# file.write(f"Hi this is  {name}")
# file.close()

# file  = open("demo1.txt","w")
# #file.write(f"Hi this is  {name}")
# print(f"hi this is {name}",file=file)
# file.close()
#file.write("ok") error..

with open("files/demo1.txt","w") as f:
    #f == fie object
    f.write(f"hi i am {name}")
    
#auto close
#f object is auto close
#f.write("ok") io operation
    