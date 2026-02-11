def marks(**kwargs):
    #kwargs is a dictionary with all the key value pairs which were passes to marks
    for items in kwargs.keys():
        print(f"the marks of {items} is {kwargs[items]}")
marks(shubham = 34, tanmay = 45, marie = 90)