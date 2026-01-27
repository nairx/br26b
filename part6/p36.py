#ducktyping
class calc:
    def display(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
try:
    c = calc()
    c.display("John")
    c.display(3)
    c.display(True)
    c.add(5,2)
    c.add(0.2,0.4)
    c.add("Hello","World")
    c.add("Hello",24)
except TypeError:
    print(f"Both arguments should be of same type.")
except Exception as e:
    print(e)