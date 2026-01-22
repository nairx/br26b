# def f1(f):
#     def wrapper():
#         print("Welcome")
#         f()
#         print("Bye")
#     return wrapper

# @f1
# def greet():
#     print("This is greet function")
# greet()



def result(marks):
    print(f"Percentage: {sum(marks) / len(marks)}")
    
marks = [90, 80, 70, 60, 50]
result(marks)