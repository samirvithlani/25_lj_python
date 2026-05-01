#delete file operation

import os
# os.remove("demo1.txt")
# print("deleted..")

#print(os.path.exists("th.txt"))
if os.path.exists("tobedeleted.txt"):
    os.remove("tobedeleted.txt")
    print("file deleyed..")
else:
    print("file not found to delete..")    