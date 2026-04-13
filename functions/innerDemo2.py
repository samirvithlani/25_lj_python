def data(*args):
    
    def processData():
        return [i**2  for i in args]
    
    return processData #address


x = data(1,2,3,4,5,6,7,8,9,10)
print(x())