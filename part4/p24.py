# def sqr(x):
#     return x * x
# result = sqr(5)

# lambda_sqr = lambda x: x * x
# result = lambda_sqr(5)

# print("The square of 5 is:", result)

# lambda_add = lambda x, y: x + y
# result = lambda_add(3, 7)       
# print("The sum of 3 and 7 is:", result)

# f1 = lambda :(x for x in range(1,15)  if x % 2 == 0)
# result = list(f1())
# print(result)  

# result = list(map(lambda x: x * x, [4,2,5,6,8]))
# print("The squares are:", result)

# result = list(filter(lambda x: x>4, [4,2,5,6,8]))
# print( result)

result = lambda x,y: x if x>y else y
print(result(10,20))