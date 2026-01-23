import array as arr
# Create an array of integers
# int_array = arr.array('i', [10, 20, 30, 40, 50])
# # Print the original array
# print("Original array:", int_array)
# # Access and print the first element    
# print("First element:", int_array[0])
# # Modify the second element
# int_array[1] = 25
# print("Modified array:", int_array)

# float_array = arr.array('f', [1.5, 2.5, 3.5, 4.5])
# # Print the original float array
# print("Original float array:", float_array)

# char_array = arr.array('u', ['a', 'b', 'c', 'd'])
# # Print the original character array
# print("Original character array:", char_array)
# # Access and print the third element    
# print("Third element:", char_array[2])

# bool_array = arr.array('b', [1, 0, 1, 1, 0])
# # Print the original boolean array
# print("Original boolean array:", bool_array)
# # Access and print the last element
# print("Last element:", bool_array[-1])
 
numbers = arr.array('i', [5, 10, 15, 20, 25])
# for i in range(len(numbers)):
#     print(numbers[i])
# numbers.append(30)
# print(numbers)
# numbers.remove(15)
# print(numbers)
# numbers.insert(2, 12)
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.extend([35, 40, 45])
# print(numbers)

num = list(numbers)
print(num)
num.sort(reverse=True)
print(num)