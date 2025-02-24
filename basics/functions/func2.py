# # # key-value argument
# # def add(x,y,z):
# #     print("x:",x)
# #     print("y:",y)
# #     print("z:",z)
# #     return x+y+z
# # p=10
# # q=20
# # r=30
# # res=add(z=p,y=q,x=r)
# # print("result:",res)
# # # positional argument
# # def add(x,y,z):
# #     print("x:",x)
# #     print("y:",y)
# #     print("z:",z)
# #     return x+y+z
# # p=10
# # q=20
# # r=30
# # res=add(r,p,q)
# # print(res)
# #default arguement
# def add(x=0,y=0,z=0):
#     print("x:",x)
#     print("y:",y)
#     print("z:",z)
#     return x+y+z
# p=10
# q=20
# r=30
# res=add()
# print(res)
# # variable length positional arguement
# def add(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# res=add(2,4,5,6,7,9,10)
# print(res)
# # # x=eval(input("Enter your values "))
# # # print(x) 
# # # print(type(x))
def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
x=eval(input("Enter your values "))
res=add(*x)
print(res)  