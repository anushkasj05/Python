# class is an example of encapsulation
# wrapping variables as well as methods in a single unit is called encapsulation
class A:
    def __init__(self):
        self.__x = 10
        self.__y = 20
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def D(self):
        print("This is a methodD of class A")
A=A()
A.D()