import os
from time import sleep
os.chdir("./part7")
# print(os.listdir())
if not os.path.isdir("newfolder"):
    os.mkdir("newfolder")
print(os.listdir())
sleep(2)
os.rmdir("newfolder")
print(os.listdir())
sleep(2)
file = open("temp.txt","w")
file.write("Hello World")
file.close
sleep(2)
print(os.listdir())
file = open("temp.txt","r")
data = file.read()
file.close()
print(data)
sleep(2)
os.remove("temp.txt")
print(os.listdir())

