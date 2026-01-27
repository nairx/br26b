from abc import ABC,abstractmethod
class Person(ABC):
    def showName(self):
        print("Printing name...")
    @abstractmethod
    def login(self):
        pass
class Employee(Person):
    def login(self,email,pwd,department):
        print("Login Successfully")
    def showSalary(self):
        print("Salary is 1000")
class Student(Person):
    def login(self,email,pwd,grade):
        print("Login Successfully")
    def showGrade(self):
        print("Grade is 3C")

e = Employee()
e.showName()
e.login("j@abc.com","1234","IT")
e.showSalary()
s = Student()
s.showName()
s.login("s@abc.com","2334","3C")
s.showGrade()

#Person > showDetails(name,age,city),login(abstract method)
#implement encapsulation by makeing name,age and city private
#Create child Class Employee and Student
#create showsalary in employee and showgrade in student
#login in both the classes