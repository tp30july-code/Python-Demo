def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_Hello(a):
    print(f"Hello!, {a}")


'''
 def decorator(func):
        def wrapper(a):
            for i in range(n):
                say_hello(a)
        return wrapper
'''

say_Hello("Harry")
