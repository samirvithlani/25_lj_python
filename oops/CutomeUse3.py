class NetworkError(Exception):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


name = "royal4"            

try:
    if name =="royal4":
        raise NetworkError("invalid wifi")
except NetworkError as e:
    print(e)    
        