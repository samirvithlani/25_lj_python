from customeEx import StringError

#if stirng is not palindrom raies string error...


name = "namita"

try:
    if name != name[::-1]:
        raise StringError("name is not plaindrome...")
except StringError as e:
    print(e)    
except ValueError:
    print("value error...")    
        
    