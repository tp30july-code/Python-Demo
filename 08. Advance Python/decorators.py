#Decorator is a function that takes a function , It creates a new function insite it body(wrapper). Then it return that new function.
def decorator(func):
    def wrapper():
        print("I am about to print Hello......!")
        func()
        print("I have excuted this function")
    return wrapper


@decorator
def say_Hello():
    print("Hello")

say_Hello()

# say_Hello()
# f = decorator(say_Hello)
# f()
     


'''
f will look something like this
def f():
    print("I am about to print Hello......!")
    print("Hello")
    print("I have excuted this function")

'''