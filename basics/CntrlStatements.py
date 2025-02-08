# Conditional Satememts
# # if
# # if-else statements
# # if-elif statements
# # if-elif-else statements
# looping/iteration Satements
# # for
# # while
#  Transfer Statements
# # break
# # continue
# # pass

# # if
# n=int(input("Enter any no."))
# if(n%2==0):
#     print(f"{n} even no")
#     print(n,"is even")
# print("Hello")
# # # if-else
# # n=int(input("Enter any no."))
# # if(n%2==0):
# #     print(f"{n} even no")
# # else:
# #     print(f"{n} odd no")
# age=int(input("Enter Your Age "))
# if(age>18):
#     print("Eligible to Vote")
# else:
#     print("Not Eligible to Vote")
# if-elif
n=float(input("Enter your Percentage"))
if n>100:
    print("Invalid Percentage")
elif n>80:
    if(n>=60):
        print("First Division")    
    elif(n>=40 and n<60):
        print("Second Division")
    elif(n>=30 and n<40):
        print("Third Division")
# if-elif-else
n=float(input("Enter your Percentage"))
if n>100:
    print("Invalid Percentage")
elif n>80:
    if(n>=60):
        print("First Division")    
    elif(n>=40 and n<60):
        print("Second Division")
    elif(n>=30 and n<40):
        print("Third Division")
    else:
        print("Fail")