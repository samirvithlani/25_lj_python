class Demo:
    
    
    x =100 #class level static variable..
    
    #self it is not a keyword
    def test(self):
        print("self",self)
        print("test function of demo class called..")
        self.no1 = 100 #instance variable... not local
        no2 = 200 #local variable
    
    def call(self):
        print(self.no1)    
        #print(self.no2) it is local variable test it can use inside test only
        


d = Demo() # demo class object
d.test() #it will pass class current object in param by default d.test(d)
print(d)
print(d.x)
#print(x)#error
print(Demo.x)

d.call()
print(d.no1)

        