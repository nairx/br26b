from time import sleep

import threading
def f1():
    for i in range(3):
        print("I am f1 function")
        sleep(3)
    
def f2():
    for i in range(3):
        print("I am f2 function")
        sleep(1)

t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()
print("Program completed successfully")


# Place Order - takes 5 seconds
# Send Email - takes 3 seconds
# Send Text Message - takes 1 second
# Finally print - Program completed successfully
# Rule:
# First order must be placed
# then email and text process should complete
# then print program completed






