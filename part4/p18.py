# def f1():
#     print("This is f1")
# f1()

# def f1(name):
#     print(f"Hello, {name}!")
# f1("John")

# def f1(name="Cathy"):
#     print(f"Hello, {name}!")
# f1()
# f1("John")

#Positional Arguments
# def f1(name,age):
#     print(f"Hello, {name}! You are {age} years old.")
# f1("John",25)

#Keyword Arguments
# def f1(name,age):
#     print(f"Hello, {name}! You are {age} years old.")
# f1(age="John",name=25)

# def f1(name,age):
#     print(f"Hello, {name}! You are {age} years old.")
# f1("John",age=25)

# def add(x,y):
#     return x+y
# result=add(5,3)
# print("The sum is:",result)

# def add(*args):
#     print("Arguments received:",args)
#     return sum(args)
# result=add(5,3,1,7,2)
# print("The sum is:",result)

# def add(**kwargs):
#     print("Arguments received:",kwargs)
#     return sum(kwargs.values())
# result=add(a=3,b=5,c=2)
# print("The sum is:",result)

# def add(*args,**kwargs):
#     print("Arguments received:",args,kwargs)
#     return sum(args) + sum(kwargs.values())
# result=add(4,6,4,2,a=3,b=5,c=2)
# print("The sum is:",result)

#score of various students
# x=10
# def f1():
#     x=5
#     print("Inside f1, x =",x)  
# f1()
# print("Outside f1, x =",x)
     
# x=10
# def f1():
#     global x
#     x=5
#     print("Inside f1, x =",x)  
# f1()
# print("Outside f1, x =",x)


# def f():
#     print("This is f function.")

# def f1():
#     print("This is f1 function.")
#     print("Hello, World!")
    
# def main(a):
#     a()
#     print("This is main function.")
#     f1()

# main(f)

#Create add, subtract, multiply, divide functions
#and main function to call them
#accept two numbers as input in main function
#and pass them to other functions