def getFullName(**kwargs):
    
    def find():
        #return kwargs.get("name")+"-"+kwargs.get("lname")
        return "-".join(list(kwargs.values()))
    
    return find()


x = getFullName(name="MahendraSingh",lname="Dhoni",nickname="thalla")
print(x)
#output mahedrasing-dhoni


    