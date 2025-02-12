# # # # break->exits from the loop
# # # # continue->stops the loop
# # # # pass->skips the loop
# # # # they are keywords
# # # # # break
# # # n=int(input("Enter any no. "))
# # # i=1
# # # while i<=n:
# # #     if i==6:
# # #         break
# # #     print(i)
# # #     i+=1
# # # continue
# # n=int(input("Enter any no. "))
# # i=1
# # while i<=n:
# #     if i==6:
# #         i=i+1
# #         continue
# #     print(i)
# #     i+=1
# # pass
# n=int(input("Enter any no. "))
# i=1
# while i<=n:
#     if i==6:
#         pass
#     print(i)
#     i+=1
# # right angled
# n=int (input("Enter the number of rows"))
# i=0
# while i<=n:
#     print("*"*i)
#     i+=1
# # left angled
# i=0
# while i<=n:
#     print(" "*(n-i)+"*"*i)
#     i+=1
# # inverted right angled triangle
# i=n
# while i>=0:
#     print("*"*i)
#     i-=1
# # inverted left angled triangle
# i=n
# while i>=0:
#     print(" "*(n-i)+"*"*i)
#     i-=1
# # pyramid 
# n=int(input("Enter the number of rows"))
# i=0
# while i<=n:
#     print(" "*(n-i)+" *"*i)
#     i+=1
# # inverted pyramid
# n=int(input("Enter the number of rows"))
# i=n
# while i>=0:
#     print(" "*(n-i)+" *"*i)
#     i-=1
# # diamond
n=int(input("Enter the number of rows"))
i=0
while i<=n:
    print(" "*(n-i)+" *"*i)
    i+=1
i=n-1
while i>=0:
    print(" "*(n-i)+" *"*i)
    i-=1