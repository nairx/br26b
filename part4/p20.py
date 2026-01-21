#list comprehension
list = [i for i in range(1,11) if i%2==0]
print(list)

#set comprehension
set1 = {i for i in range(1,11) if i%2!=0}
print(set1)

#dictionary comprehension
dict1 = {i:f"item{i}" for i in range(1,5)}
print(dict1)

names = ['apple', 'banana', 'cherry']
prices = [100, 200, 300]
fruit_dict = {names[i]: prices[i] for i in range(len(names))}
print(fruit_dict)


