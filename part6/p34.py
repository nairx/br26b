class Person:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def showDetails(self):
        print(self.name,self.age)
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
    def showSalary(self):
        print(self.salary)
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    def showGrade(self):
        print(self.grade)
e = Employee("John",21,1000)
e.showDetails()
e.showSalary()
s=Student("Amy",14,"5C")
s.showDetails()
s.showGrade()
