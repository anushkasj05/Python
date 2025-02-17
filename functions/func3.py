# def add(*n):
#     sum=0
#     for i in n:
#         print(i)
#         for j in i:
#             sum+=j
#     return sum
# x=eval(input("Enter any collection"))
# res=add(x)
# print(res)
# def add(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# res=add(z=10,y=20,x=30,p=5,q=15)
# print(res) 
def add(**kwargs):
    print(kwargs)
x=eval(input("Enter your dict: "))
res=add(**x)