
def paytm(amount):
    print("pay via paytm",amount)

def phonepe(amount):    
    print("pay via phonpe",amount)

def fampay(amount):    
    print("pay via fampay",amount)    

    
def paynow(fun,amount):
    print("paynow called..")
    fun(amount) #phonpe



appname = input("enter app Name: ")
amount = int(input("enter amount :"))

if appname == "phonepe":
    paynow(phonepe,amount)
elif appname=="fampay":
    paynow(fampay,amount)
elif appname ==  "paytm":
    paynow(paytm,amount)
