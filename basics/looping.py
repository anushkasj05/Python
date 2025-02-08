# # while-loop->infinte iterations/finite iterations
# # for loop->finite iteration
# i=0
# while(i<=10):
#     print(i)
#     i=i+1
n=int(input("Enter any no."))
i=1
while(i<=n):
    if(i<n):
        print(i,end=',')
    else:
        print(i)
    i=i+1
n = int(input("Enter any number: "))
for i in range(1, n + 1):
    if i < n:
        print(i, end=',')
    else:
        print(i)