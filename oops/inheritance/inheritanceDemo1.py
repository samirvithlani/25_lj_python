#single -->A -->B
class Color:
    
    def hash(self):
        print("i am hash of any color")
        self.code ="FFFFF"

class White(Color):
    
    def show(self):
        return self.code


w = White()    
w.show()
    
            