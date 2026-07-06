from CustException import InvalidDataError
try:
    no =int(input("enter no"))
    if(no<0):
        raise InvalidDataError("value must be positive !!")
    
    print(no)
except ValueError as e:
    print(e)
except InvalidDataError as e:
    print(e)         

