def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False
    
a = [1, 3, 6, 3, 4, 2, 6, 5 ,4 , 34 , 23 , 2 , 4, 5 ,6 , 7, 8, 9]

new = list(filter(is_greater_than_9, a))
print(new)