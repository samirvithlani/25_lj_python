class Cart:
    
    def __init__(self,items):
        self.items = items
    
    # + op overload
    def __add__(self, other):
        #self -->left side op --> other -->right side op
        print("self",self.items)
        print("other",other.items)
        return Cart(self.items + other.items)


cart1 =Cart([{"name":"iphone","price":1200}])        
cart2 =Cart([{"name":"ipad","price":1400}])        


# + -> __add__()
final = cart1 + cart2
print(final.items)
