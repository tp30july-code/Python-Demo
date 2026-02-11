def sum(a,b):
    c = a + b
    z = 1 #here z is a local variable
    return c

def greet():
    z = 32 #local variable
    print("Hello")

print(sum(4,6))
z = 8
print(z)