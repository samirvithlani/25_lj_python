def demo(x):
    if len(x)>4:
        return x.upper()
    else:
        return x

users = ["ajay","raj","parth","sumit"]

ans  =map(lambda x: demo(x),users)
print(list(ans))
