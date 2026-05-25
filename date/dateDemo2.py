from datetime import date

today = date.today()
#y Y B b a
print(today.strftime("%d/%m/%Y"))
print(today.strftime("%a"))
print(today.strftime("%B"))
print(today.strftime("%H")) #24
print(today.strftime("%I")) #12
print(today.strftime("%M"))
print(today.strftime("%S"))
print(today.strftime("%p"))