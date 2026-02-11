a = 24
b = "24"
print(a)
print(type(a))

print(b)
print(type(b))
#here a and b have same value but different data type because we have use double quote in b

#conversion of the data type
c = int(b) #here we have convert string to integer  
print(type(c))

#we can also convert integer to string
d = str(a)
print(type(d))

#convert float to integer
e = 24.32
e = int(e)
print(e)# it has remove all the value after the decimal point
print(type(e))