# a special type of method that does not have to be called as it is itself called when the object is created
# self is a reference variable that holds the current address of the current object
class Student:
    def __init__(self):
        print("Constructor called")
# obj=Student # nothing will come
obj=Student() # Constructor called