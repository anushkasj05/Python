# # syntex
# # filter(fun-name,iterator)
# # collecion-string-list-tupple
# even/odd
# l1=eval(input("Enter a collection: "))
# def myeven(n):
#     if n%2==0:
#         return n
# x=list(filter(myeven,l1))
# print(x)  # [2, 4, 6, 8, 10]
# prime number
l1=eval(input("Enter a collection: "))
def myprime(n):
    for i in range(2,n):
        if n%i!=0:
            return n
        break
x=list(filter(myprime,l1))
print(x)  # [2, 3, 5, 7, 11]