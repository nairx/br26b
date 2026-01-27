class Calc:
    def greet(self,name=None):
        if name != None:
            print(f"Hello {name}")
        else:
            print("Hello")
            
c = Calc()
c.greet()
c.greet("John")
            