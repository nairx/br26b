from collections import UserString

class MyStr(UserString):
    def upper(self,s=None):
        raise Exception("Upper method not allowed")
        # return self.data
    def lower(self,s=None):
        return super().upper()
    def greet(self):
        print(self.data)

str = MyStr("Hello World")

# print(str.upper())
print(str.lower())
print(str.greet())

#when lower method is called
#the reslt must be in uppercase