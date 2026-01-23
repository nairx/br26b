class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
    def get_grade(self):
        if self.salary >= 5000:
            return "A"
        else: 
            return "B"
    def __del__(self):
        print(f"Employee {self.name} is being deleted.")

e = Employee("John", 21,1000)
print(e.get_details())
print("Grade:", e.get_grade())

# del e

#BankAccount class and add deposit 
# method and withdraw method



