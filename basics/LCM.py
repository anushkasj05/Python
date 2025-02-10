n1=int(input("Enter number1 "))
n2=int(input("Enter number2 "))
n3=int(input("Enter number3 "))
max=max(n1,n2,n3)
i=1
j=1
while True:
    if max%n1==0 and max%n2==0 and max%n3==0:
        j+=1
        print(j)
        break
    i+=1
    max=max*i
print(f'LCM of {n1}, {n2} and {n3} is {max}')
