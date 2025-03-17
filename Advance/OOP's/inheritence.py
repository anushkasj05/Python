# # # # # # the parent child relationship is called inheritence
# # # # # # single inheritence
# # # # # class A:
# # # # #     x=5
# # # # #     def home(self):
# # # # #         print("A home")
# # # # # class B(A):
# # # # #     def house(self):
# # # # #         print("B house")
# # # # # obj=B()
# # # # # obj.home()
# # # # # print(obj.x)
# # # ##############################################################################################################
# # # # # multiple inheritence
# # # # MRO ->method resolution order
# # # # class A:
# # # #     x=5
# # # #     def home(self):
# # # #         print("A home")
# # # # class B:
# # # #     y=10
# # # #     def house(self):
# # # #         print("B house")
# # # # class C(A,B): #method resolution order the left parent is given the priority
# # # #     def hoome(self):
# # # #         print("C home")
# # # # obj=C()
# # # # obj.home()
# # # # print(obj.x)
# # # # obj.house()
# # # # print(obj.y)
# # # ##############################################################################################################
# # # # method overidinging is done when there are methods with the same name 
# # # class Parent:
# # #     def home(self):
# # #         print("Parent home")
# # # class Child(Parent):
# # #     def home(self):
# # #         print("Child home")
# # #         super().home()
# # # obj=Child()
# # # obj.home()
# # # ##############################################################################################################
# # # # multi level inheritence
# # # class A:
# # #     x=5
# # #     def home(self):
# # #         print("A home")
# # # class B(A):
# # #     y=10
# # #     def house(self):
# # #         print("B house")
# # # class C(B):
# # #     def house(self):
# # #         print("C home")
# # #         super().house()
# # # obj=C()
# # # obj.home()
# # # obj.house()
# # # ##############################################################################################################
# # # class A:
# # #     x=5
# # #     def home(self):
# # #         print("A home")
# # # class B(A):
# # #     y=10
# # #     def home(self):
# # #         print("B house")
# # # class C(B):
# # #     def home(self):
# # #         print("C home")
# # #         super(B,obj).home()
# # # obj=C()
# # # obj.home()

# # # ##############################################################################################################
# hybrid  
class A:
    def home(self):
        print("A home")
class B(A):
    def house(self):
        print("B house")
class C(A):
    def hoome(self):
        print("C home")
class D(B,C):
    def hoome(self):                
        super().hoome()
        print("D home")
obj=D()
obj.home()
obj.house()
obj.hoome()
# # ###########################################################################################################
# # # method overriding
# # class A:
# #     def new(self):
# #         print("Hello")
# # class B(A):
# #     def new(self):
# #         print("from child class")
# #         super().new()
# # obj=B()
# # obj.new()
# ###########################################################################################################
# # hierarical
# class A:
#     def new(self):
#         print("Class A")
# class B(A):
#     def newB(self):
#         print("Class B")
#         # super().new()
# class C(A):
#     def newC(self):
#         print("Class C")
#         # super().new()
# class D(A):
#     def newD(self):
#         print("Class D")
#         # super().new()
# Bobj=B()
# Bobj.newB()
# Bobj.new()
# Cobj=C()
# Cobj.newC()
# Cobj.new()
# Dobj=D()
# Dobj.newD()
# Dobj.new()