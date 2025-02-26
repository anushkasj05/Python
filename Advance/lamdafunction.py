# # # # # # # a function without name 
# # # # # # # use lambda keyword instead of the def keyword
# # # # # # # it takes n number of arguments
# # # # # # # but executes a single line of expression
# # # # # # # syntex:-
# # # # # # # lambda arguements:expressions
# # # # # # # wap to add two numbers
# # # # # # x=eval(input("Enter a number: "))
# # # # # # y=eval(input("Enter a number: "))
# # # # # # res=lambda p,q:p+q
# # # # # # print("Addition of two numbers is:",res(x,y))  
# # # # # # another method
# # # # # x=eval(input("Enter number1 "))
# # # # # y=eval(input("Enter number2 "))
# # # # # res=lambda p,q:print(p+q)
# # # # # res(x,y)
# # # # # even or odd
# # # # x=eval(input("Enter a number: "))
# # # # res=lambda p:print("Even") if p%2==0 else print("Odd")
# # # # res(x)
# # # l1=[]
# # # for i in range(1,4):
# # #     l1.append(i)
# # # l2=[]
# # # for i in range(3):
# # #     l2.append(l1)
# # # print (l2)
# # # # # # # # # # # # # # # # # # # # # #
# # # using lambda function the same function
# # # syntex:-
# # # lambda x: [i for i in collection]-> list comprehensing
# # x="Anushka"
# # z =lambda x:[p for p in x]
# # print(z(x))
# # # # # # # # # # # # # # # # # # # # #
# x = [1, 2, 3]
# res = lambda p: [p for _ in range(4)]
# print(res(x))
# # # # # # # # # # # # # # # # # # # #
x=[4]
res=lambda p:[i for i in range(i,p) for k in range(4)]
print(res(x))

