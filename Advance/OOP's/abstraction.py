# # from abc import ABC,abstractmethod
# # class A(ABC):
# #     def new(self):
# #         print("80%")
# #     @abstractmethod
# #     def new1(self):
# #         pass
# # class B(A):
# #     def first(self):
# #         print("20%")
# # obj=B()
# # obj.new()
# from abc import ABC,abstractmethod
# class bank(ABC):
#     def registration(self):
#         print("Registration")
#     def logout(self):
#         print("Logout")
#     @abstractmethod
#     def authentication(self):
#         pass
#     def dashboard(self):
#         print("Dashboard")
# class WebApp(bank):
#     def login(self,id,psw):
#         self.id=id
#         self.pasw=psw
# obj=WebApp()
# obj.dashboard()
# obj.login(101,123)

from abc import ABC,abstractmethod
class bank(ABC):
    def registration(self):
        print("Registration")
    def logout(self):
        print("Logout")
    @abstractmethod
    def authentication(self):
        pass
    def dashboard(self):
        print("Dashboard")
class WebApp(bank):
    def login(self,id,psw):
        self.id=id
        self.pasw=psw
    def authentication(self):
        print("Authenication")
obj=WebApp()
obj.dashboard()
obj.login(101,123)