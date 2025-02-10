n = 10
i = 1
sum_even = 0  

while i <= n:
    if i % 2 == 0:
        sum_even += i  
        if i < n:
            print(i, end='+')
        else:
            print(i,end='=')
    i += 1

print(sum_even)
