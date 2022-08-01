#hw 8-2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, a, b):
       self.a = a
       self.b = b
    

    def get_area(self):
        s = abs(self.a.x-self.b.x)*abs(self.a.y-self.b.y)
        return s

    def get_perimeter(self):
        p = (abs(self.a.x-self.b.x)+abs(self.a.y-self.b.y))*2
        return p

    def is_square(self):
        if abs(self.a.x-self.b.x) == abs(self.a.y-self.b.y):
            return True
        else:
            return False

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())






