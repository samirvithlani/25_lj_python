def calc(*args):
    op = args[0]
    ans=0
    match op:
        case "+":
            for i in args[1:]:
                ans = ans+i
            return ans
        case "-":
            ans = args[len(args)-1] #5
            for i in args[-2:0:-1]:
                ans = ans - i
            return ans    
x = calc("-",1,2,3,4,5)
print(x)