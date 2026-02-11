from time import time

def timer(func):
    def wrapper(n):
        t1 = time()
        func(n)
        t2 = time()
        print(t2 - t1)
    return wrapper

@timer
def sum_1m(n):
    sum = 0
    for i in range(1, 1+n):
        sum += i 
    return sum

a = sum_1m(100000)
print(a)