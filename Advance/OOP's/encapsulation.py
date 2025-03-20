# class is an example of encapsulation
# wrapping variables as well as methods in a single unit is called encapsulation
class Book:
    price=100
    def __init__(self,name):
        self.author=name
    def add(self,total_pages):
        self.pages=total_pages
    @classmethod
    def update_price(cls,x):
        p="Hello"
        cls.price=x
    @staticmethod
    def greet():
        print("Welcome to my web page")
obj=Book()
obj.add(200)
print(obj.price)
Book.update_price(500)
print(Book.price)
Book.greet()  # static method can be called without creating an object