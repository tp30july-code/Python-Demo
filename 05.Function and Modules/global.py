def sum(a, b):
    print("Hey I am summing")
    c = a + b
    global z #plz multiply global z
    z = 0 #this will br refer to global z and will not be  store as a local variable
    return c

z=3
print(sum(3, 12))
print(z)