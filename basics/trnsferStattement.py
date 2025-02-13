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
n=int(input("Enter any no. "))
# i=1
# while i<=n:
#     if i==6:
#         pass
#     print(i)
#     i+=1
# # right angled
print("1 right angles")
i=0
while i<=n:
    print("*"*i)
    i+=1
# # left angled
print("2 left angled")
i=0
while i<=n:
    print(" "*(n-i)+"*"*i)
    i+=1
# # pyramid 
print("3 pyramid")
i=0
while i<=n:
    print(" "*(n-i)+" *"*i)
    i+=1
# # inverted right angled triangle
print("4 inverted right angled triangle")
i=n
while i>=0:
    print("*"*i)
    i-=1
# # inverted left angled triangle
print("5 inverted left angled triangle")
i=n
while i>=0:
    print(" "*(n-i)+"*"*i)
    i-=1
# # inverted pyramid
print("6 inverted pyramid")
i=n
while i>=0:
    print(" "*(n-i)+" *"*i)
    i-=1
# # inverted right angled triangle
print("7 ")
i=n
while i > 0:
    print('*' * i)
    i -= 1
i = 2
while i <= n:
    print('*' * i)
    i += 1
print("8")
i=0
while i<=n:
    print(" "*(n-i)+"*"*i)
    i+=1
i=n-1
while i>=0:
    print("*"*i)
    i-=1
print("9")
i=0
while i<=n:
    print("*"*i)
    i+=1
i=n-1
while i>=0:
    print(" "*(n-i)+"*"*i)
    i-=1
# # diamond
print("10 diamond")
i=0
while i<=n:
    print(" "*(n-i)+" *"*i)
    i+=1
i=n-1
while i>=0:
    print(" "*(n-i)+" *"*i)
    i-=1
# #
print("11")
i = n
while i >= 1:#1
    print(" " * (n - i) + "*" * i)
    i -= 1
i = 2
while i <= n:
    print(" " * (n - i) + "*" * i)
    i += 1
i = n
print("12")
i=n
while i>=1:
    print(" "*(n-i)+" *"*i)
    i-=1
i=2
while i<=n:
    print(" "*(n-i)+" *"*i)
    i+=1
