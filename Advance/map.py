# # # # it is a higher order function
# # # # the function in which a function is passed as an argument of another function 
# # # # than the initaial function is called the higher order function
# # # #  
# # # # sytex:-
# # # # map(fun-name,iterator)
# # # # iterator->collection 
# # # # -string -list -tuple -set -dict
# # # x=eval(input("Enter any collection: "))
# # # l1=[]
# # # for i in x:
# # #     i=i**2
# # #     l1.append(i)
# # # print(l1)
# # def sqr(n):
# #     return n*n
# # l1=eval(input("Enter any collection: "))
# # x=map(sqr,l1)
# # print(list(x))
# # print(x)#returns the object of the map
# def sqr(n):
#     return n+5
# l1=eval(input("Enter any collection: "))
# x=map(sqr,l1)
# print(list(x))
# print(x)#returns the object of the map
# # # # # # # # # # # # # # # # # # # #
# how many time are the internal loops running?
# the lowest number of the iterations that is 3
# only map can have many number of iterators
l1=eval(input("Enter collection1: ")) #[1,2,3,4,5]
l2=eval(input("Enter collection2: ")) #[1,2,3,4]
l3=eval(input("Enter collection3: ")) #[1,2,3]
def add(x,y,z):
    return x+y+z
x=map(add,l1,l2,l3)
print(list(x))