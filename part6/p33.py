class Person:
    def showName(self,name):
        print(name)
        
class Staff(Person):
    def showSalary(self,salary):
        print(salary)

class Contractor(Person):
    def showWage(self,wage):
        print(wage)
  
s = Staff()
s.showName("John")
s.showSalary(1000)
c = Contractor()
c.showName("Mike")
c.showWage(500)