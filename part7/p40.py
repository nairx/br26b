# file = open("./part7/file.txt","w")
# file.write("Hello World")

# file = open("./part7/file.txt","a")
# file.write("Hello World\n")
# file.close()

# file = open("./part7/file.txt","r")
# data = file.read()
# print(data)

#Accept name,email,city,phone from user
#and add the details in a text file
#Loop through the task as long as user wants to continue

while True:
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    city=input("Enter your city: ")
    phone=input("Enter your phone: ")
    file=open("./part7/file.txt","a")
    file.write(f"{name},{email},{city},{phone}\n")
    file.close()
    cont=input("Do you want to continue? (yes/no): ")
    if cont.lower()!="yes":
        break
file = open("./part7/file.txt", "r")
data = file.read()
file.close()
 
print(data)