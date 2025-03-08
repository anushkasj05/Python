# # # types of methods
# # # 1. instance methods (self)
# # # 2. class methods    (class)
# # # 3. static methods   (X)
# # # Instance Methods
# # class Student:
# #     def first(self):
# #         print("this is from first")
# #     def second(self):
# #         #Student.first(self)
# #         obj1=Student
# #         obj1.first()
# # obj=Student()
# # obj.first()
# # obj.second()
# ###########################################################################################################
# # # Class Methods(directly related to class)
# # why we use
# # to modify static/class variable we use class method
# # we use @classmethod
# # the first parameter is cls
# # cls=class
# class Book:
#     price=100
#     total_pages=500
#     def __init__(self,author):
#         self.Author=author
#         print(self.Author,Book.price,Book.total_pages)
#     @classmethod
#     def update(cls,p,q):
#         cls.price=p
#         cls.total_pages=q
# p=input("Enter the Price ")
# q=input("Enter the Total Pages ")
# Book.update(p,q)
# obj1=Book('Anushka')
# p=input("Enter the Price ")
# q=input("Enter the Total Pages ")
# Book.update(p,q)
# obj2=Book('Divyansh')
############################################################################################################
# Static Methods 
# we use @staticmethod
class Book:
    def __init__(self):
        print("Constructor called")
    @staticmethod
    def welcome(self):
        print("Welcome to Python")
    @staticmethod
    def thanks():
        print("Thanks for Visit")