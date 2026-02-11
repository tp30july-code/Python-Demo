def logger(func):
    def wrapper():
        print("Function is been callled")
        func()
    return wrapper

@logger
def say_hello():
    print("Hello")

