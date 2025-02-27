# # # # # # # # # # # # # a function without name 
# # # # # # # # # # # # # use lambda keyword instead of the def keyword
# # # # # # # # # # # # # it takes n number of arguments
# # # # # # # # # # # # # but executes a single line of expression
# # # # # # # # # # # # # syntex:-
# # # # # # # # # # # # # lambda arguements:expressions
# # # # # # # # # # # # # wap to add two numbers
# # # # # # # # # # # # x=eval(input("Enter a number: "))
# # # # # # # # # # # # y=eval(input("Enter a number: "))
# # # # # # # # # # # # res=lambda p,q:p+q
# # # # # # # # # # # # print("Addition of two numbers is:",res(x,y))  
# # # # # # # # # # # # another method
# # # # # # # # # # # x=eval(input("Enter number1 "))
# # # # # # # # # # # y=eval(input("Enter number2 "))
# # # # # # # # # # # res=lambda p,q:print(p+q)
# # # # # # # # # # # res(x,y)
# # # # # # # # # # # even or odd
# # # # # # # # # # x=eval(input("Enter a number: "))
# # # # # # # # # # res=lambda p:print("Even") if p%2==0 else print("Odd")
# # # # # # # # # # res(x)
# # # # # # # # # l1=[]
# # # # # # # # # for i in range(1,4):
# # # # # # # # #     l1.append(i)
# # # # # # # # # l2=[]
# # # # # # # # # for i in range(3):
# # # # # # # # #     l2.append(l1)
# # # # # # # # # print (l2)
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # using lambda function the same function
# # # # # # # # # syntex:-
# # # # # # # # # lambda x: [i for i in collection]-> list comprehensing
# # # # # # # # x="Anushka"
# # # # # # # # z =lambda x:[p for p in x]
# # # # # # # # print(z(x))
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # x = [1, 2, 3]
# # # # # # # res = lambda p: [p for _ in range(4)]
# # # # # # # print(res(x))
# # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # x=4
# # # # # # res=lambda p:[[i for i in range(1,p)] for k in range(p)] #why we use k we can use _
# # # # # # print(res(x))
# # # # # for _ in range(4):
# # # # #     print("Hello")
# # # # ##################################################
# # # # #  lambda with map
# # # # # l1=[1,2,3,4]
# # # # # def my_sqr(n):
# # # # #     return n*n
# # # # # res=list(map(my_sqr,l1))
# # # # # print(res)
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # l1=[1,2,3,4]
# # # # res=list(map(lambda n:n*n,l1))
# # # # print (res)
# # # # # # # # # # # # # # # # # # # # # # #
# # # # map+lambda+if else 
# # # l1=[1,2,3,4]
# # # res=list(map(lambda res: 'even' if res%2==0 else 'odd',l1))
# # # print(res)
# # # # # # # # # # # # # # # # # # # # # #
# # # filter+lambda+if else+none
# # l1=[1,2,3,4]
# # res=list(filter(lambda res: res if res%2!=0 else None,l1))
# # print(res) 
# # # # # # # # # # # # # # # # # # # # #\
# # reduce+labda+max number
# # from functools import reduce 
# # l1=[12,5,10,17]
# # x=reduce(lambda x,y:x if x>y else y,l1)
# # print(x)
# # reduce+labda+min number
# # from functools import reduce 
# # l1=[12,5,10,17]
# # x=reduce(lambda x,y:x if x<y else y,l1)
# # print(x)
# # # reduce+labda+sum
# from functools import reduce
# l1=[12,5,10,17]
# x=reduce(lambda x,y:x+y,l1)
# print(x)
x=lambda p :[i for i in range(2,11,2)]
print(x(10))