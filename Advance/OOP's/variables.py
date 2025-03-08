# # # # variables
# # # # -Static  
# # # # -local
# # # # -instance(object dependent variable)those variables which are changing the value as we change the object
# # # class Students:
# # #     def __init__(self, name, marks):
# # #         self.x = name # instance variable
# # #         self.y = marks # instance variable
# # #     def show(self):
# # #         print(self.x)
# # #         print(self.y)
# # # obj=Students("Anushka",5)
# # # # print(obj.x)
# # # # print(obj.y)
# # # obj.show()
# # # obj1=Students("Divyansh",12)
# # # obj1.show()
# # # # # can we declare instance variable outside of the class?
# # # # # yes we can 
# # # # class Students:
# # # #     def __init__(self):
# # # #         print("display method")
# # # #     def show(self):
# # # #         print("Value of x ",self.x)
# # # # obj=Students()
# # # # obj.x=10
# # # # obj.show()
# # # # with the help of self we can access the variable inside the class
# # # # with the help of object we can access the variable outside the class
# # ####################################################################################################
# # # static/class variable(a variable that is not dependent on the object)
# # class Student:
# #     school='SHSS'
# #     city='Bhopal'
# #     def __init__(self, name, rol):
# #         self.x=name
# #         self.y=rol
# #     def show(self):
# #         print(self.x,self.y)
# #         print(Student.school) # class/static variable
# #         print(Student.city)   # class/static variable
# # obj=Student('Anushka',12)
# # obj.show()
# # obj2=Student('Divyansh',5)
# # obj2.show()
# # # static variables can be declared 
# # # -inside class 
# # #   -outside method
# # #   -inside instance method   # from class name
# # #   -inside constructor       # from class name
# # # -outside class              # from class name
# # where can we call static variables
# # -inside class
# # - outside class
# class Student:
#     school='SHSS' # static/class variable
#     def __init__(self,name,roll):
#         self.x=name
#         self.y=roll
#         Student.city='Bhopal'  # static/class variable
#     def show(self):
#         Student.s_code=123     # static/class variable
#     def display(self):
#         print(Student.s_code)    # Called
#         print(Student.city)      # Called
#         print(Student.school)    # Called
#         print(Student.principal) # Called
# Student.principal="DC"        # static/class variable
# obj=Student('Anushka',12)
# obj.show()
# obj.display()
# print(Student.school)        # Called
# #####################################################################################################
# local variable (variable that can we accessed within the block)
class Student:
    school='SHSS' # static/class variable
    def __init__(self,name,roll):
        self.x=name
        self.y=roll
        Student.city='Bhopal'  # static/class variable
    def show(self):
        Student.s_code=123     # static/class variable
        p=10
        print(p) # p is a local variable
    def display(self):
        print(Student.s_code)    # Called
        print(Student.city)      # Called
        print(Student.school)    # Called
        print(Student.principal) # Called
Student.principal="DC"        # static/class variable
obj=Student('Anushka',12)
obj.show()
obj.display()
print(Student.school)  