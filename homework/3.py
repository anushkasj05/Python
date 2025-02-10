n = 10
i = 1

while i <= n:
    if i % 2 == 0:
        if i < n:
            print(i, end=',')
        else:
            print(i)
    i += 1
