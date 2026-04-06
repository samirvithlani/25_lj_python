
def paytm():
    print("pay via paytm")

def phonepe():    
    print("pay via phonpe")

def fampay():    
    print("pay via fampay")    

    
def paynow(fun):
    print("paynow called..")
    fun()



appname = input("enter app Name: ")
if appname == "phonepe":
    paynow(phonepe)
elif appname=="fampay":
    paynow(fampay)
elif appname ==  "paytm":
    paynow(paytm)
