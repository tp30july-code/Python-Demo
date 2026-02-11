coordinate = (10,20)

print(coordinate[0])
print(coordinate[1])

corlist = list(coordinate)
corlist[0] = 50
coordinate = tuple(corlist)
print(coordinate)