# # # it returns an iterator type of object 
# # # whenever we use yield in place of return
# # yield is only used in the generator
# yield is used in generator whereas return is used in function
# memory used will be less 
# # def first():
# #     yield 'Hello'
# # def first2():
# #     return 'World'
# # x=first()
# # print(x)
# # y=first2()
# # print(y)
# def first():
#     yield 1
#     yield 2
#     yield 3
# x=first()
# print(next(x))
# print("Hi")
# print("Hello")
# print("Welcome")
# print(next(x))
# print(next(x)) 
def natural(n):
    i=1
    while i<=n:
        yield i
        i+=1
n=int(input("Enter the number: "))
p=natural(n)
# print(p)
# print(list(p))
print(next(p))
print(next(p))
for i in p:
    print(i)  