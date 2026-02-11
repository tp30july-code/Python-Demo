number = [1, 2, 3 , 4, 7, 21, 34, 45]

def square(x):
    return x*x

new = list(map(square, number))
print(new)