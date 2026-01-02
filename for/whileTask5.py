chance =3
bal = 0
while chance>0:
    bal = int(input("enter bal :"))
    if(bal>=10000):
        print("acoount has been opened")
        break
    else:
        print("try again latter !!")    
        chance-=1

        