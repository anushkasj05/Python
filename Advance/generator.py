# # it returns an iterator type of object 
# # whenever we use yield in place of return
# def first():
#     yield 'Hello'
# def first2():
#     return 'World'
# x=first()
# print(x)
# y=first2()
# print(y)
def first():
    yield 1
    yield 2
    yield 3
x=first()
print(next(x))
print("Hi")
print("Hello")
print("Welcome")
print(next(x))
print(next(x)) 