from time import sleep
import threading
def sqr(num):
    print(f"Square is {num*num}")
    sleep(3)
def cube(num):
    print(f"Cube is {num*num*num}")
    sleep(2)
t1 = threading.Thread(target=sqr,args=(5,))
t2 = threading.Thread(target=cube,args=(3,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Program Completed Successfully")

