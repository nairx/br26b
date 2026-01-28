from collections import UserList

class MyList(UserList):
    def pop(self,s=None):
        raise Exception("Pop not allowed")

numbers = MyList([5,7,6,4])
numbers.pop()
# print(numbers)


#pop should not be allowed