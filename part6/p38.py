class Employee:
    a = 10
    def __init__(self,name):
        self.__name = name
    def getName(self):
        print(self.__name)
    def setName(self,name):
        self.__name = name
        
e = Employee("John")
e.getName()
e.setName("Cathy")
e.getName()

print(Employee.a)
Employee.a = 20
print(Employee.a)



    