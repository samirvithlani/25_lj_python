from CustException import InvalidDataError

no = 123
try:
    if type(no)==int:
        raise InvalidDataError("data is invalud.")
except InvalidDataError as e:
    print(e)    


    