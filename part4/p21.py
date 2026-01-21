import sys
#methon 1 of creating generator
# def count_up_to():
#     for i in range(10):
#         yield i
# result = count_up_to()

#method 2 of creating generator
# result = (x for x in range(100))
# print(type(result))

#method 3 of creating generator
l = [x for x in range(100)]
result = iter(l)
print(type(result))

list = [x for x in range(100)]
print(type(list))

# for i in result:
#     print(i)

print(sys.getsizeof(list))  
print(sys.getsizeof(result))

    

    


