from customeEx import StringError
email = "ram_gmail.com"

try:
    if "@" not in email:
        raise StringError("email is in valid..")
    print("email ",email)
except StringError as e:
    print(e)    