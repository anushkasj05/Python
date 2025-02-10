sum = 0
num = 0
while True:
    sum += num
    print(num, end='+')
    num += 1
    if num >= 10:
        print(num, end='=')
        print(sum)
        break
