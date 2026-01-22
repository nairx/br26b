# def sqr(x):
#     return x * x    
# list2 = list(map(sqr, [1, 2, 3, 4, 5]))
# print(list2)  

# def f1(x):
#     return x%2==0    
# list2 = list(filter(f1, [1, 2, 3, 4, 5]))
# print(list2)  

# from functools import reduce
# def f1(x,y):
#     return x+y   
# total = reduce(f1, [1, 2, 3, 4, 5])
# print(total)  

# names = ['John', 'Lisa', 'Amy']
# scores = [95, 85, 76]
# result = zip(names, scores)
# print(list(result))
# for i, j in zip(names, scores):
#     print(i,j)

# names = ['John', 'Lisa', 'Amy']
# for i, j in enumerate(names,start=1):
#     print(i,j)

# list = [x for x in range(100)]
# print(list)

list = list(range(100))
print(list)