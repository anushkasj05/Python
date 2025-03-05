# a special type of method that does not have to be called as it is itself called when the object is created
# self is a reference variable that holds the current address of the current object
# we can make n number of constructor but with different name (not important to do so but to avoid constructor overloading)
# without constructor class object can't be created
# in a class makinmg a constructor is not important as it will have a default constructor
# () is responsible for calling the constructor
class Student:
    def __init__(self):
        print("Constructor called")
    def __init__(self):
        print("Another constructor called")
# obj=Student # nothing will come
obj=Student() # Constructor called    # Another constructor called
# obj.__init__()