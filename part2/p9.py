# counter = 1
# while counter < 5:
#     print(counter)
#     counter = counter + 1
    
# counter = 1
# while counter < 5:
#     print(counter)
#     counter = counter + 1
#     if counter == 3:
#         break
# else:
#     print("Program completed successfully")

# counter = 1
# while counter < 5:
#     num = int(input("Enter number"))
#     counter = counter + 1
#     if num == 3:
#         break   
# else:
#     print("Program competed successfully")
    
# while True:
#     num = int(input("Enter number"))
#     if num == 3:
#         break   
#     print(f"You have entered {num}")
    
counter = 1
while counter < 5:
    num = int(input("Enter number"))
    counter = counter + 1
    if num == 3:
        continue
    print(f"You have entered {num}")