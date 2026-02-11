def sum(*args):#args will be the tuple of all the value passed to sum
    print(args)
    total = 0
    for item in args:
        total += item
    return total

print(sum(324, 34, 56, 9, 10))