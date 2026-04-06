

def test(a):
    print("test called..")
    print(a)
    a()

def callling():
    print("calling called....")

# test("abc")    
# test(123)
# test((1,2,3))
test(callling)