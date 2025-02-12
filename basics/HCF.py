# n1=int(input("Enter number1 "))
# n2=int(input("Enter number2 "))
# n3=int(input("Enter number3 "))
# min=min(n1,n2,n3)
# i=1
# # while True:
# #     if n1%min==0 and n2%min==0 and n3%min==0:
# #         i+=1
# #         print('Loop{i}')
# #         break
# #     min=min-1
# # print(min)
# q=1
# while i>=min:
#     if n1%i==0 and n2%i==0 and n3%i==0:
#         q=q*i
#         i+=1    
x=int(input("Enter the number "))
y=int(input("Enter the number "))
m=min(x,y)
while m>0:
    if x%m==0 and y%m==0:
        hcf=m
        break
    m=m-1
print("hcf = ",hcf)