# reduce(fun-name,iterator)
# there are two ways 
# import functools
# from functools import reduce
# reduce(fun-name,iterator)
from functools import reduce
l1=eval(input("Enter collection: "))
def mymax(x,y):
    if x>y:
        return x
    else:
        return y
p=reduce(mymax,l1)
print("The maximum value is:",p)  # output: The maximum value is: 10