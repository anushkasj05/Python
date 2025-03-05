# # variables
# # -Static  
# # -instance(object dependent variable)those variables which are changing the value as we change the object
# # -local
# class Students:
#     def __init__(self, name, marks):
#         self.x = name # instance variable
#         self.y = marks # instance variable
#     def show(self):
#         print(self.x)
#         print(self.y)
# obj=Students("Anushka",5)
# # print(obj.x)
# # print(obj.y)
# obj.show()
# obj1=Students("Divyansh",12)
# obj1.show()
# # # can we declare instance variable outside of the class?
# # # yes we can 
# # class Students:
# #     def __init__(self):
# #         print("display method")
# #     def show(self):
# #         print("Value of x ",self.x)
# # obj=Students()
# # obj.x=10
# # obj.show()
# # with the help of self we can access the variable inside the class
# # with the help of object we can access the variable outside the class
####################################################################################################
# static/class variable(a variable that is not dependent on the object)