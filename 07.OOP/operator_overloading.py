class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def print_point(self):
        return (f"X id {self.x}i and y is {self.y}j")

p1 = Point(3, 2)
p2 = Point(9, 5)
p = p1.sum(p2)#return a new point
print(p.x, p.y)
p.print_point()