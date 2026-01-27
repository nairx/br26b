#Method Overriding
class User:
    def greet(self):
        print("Hello")
        
class Employee(User):
    def greet(self):
        print("Good Day!")

class Student(User):
    def welcome(self):
        print("Welcome to the Party")

e = Employee()
e.greet()
s = Student()
s.greet()
s.welcome()