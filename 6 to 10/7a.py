import math
class Shape:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        s = "{}".format(self.name)
        return s
class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__('Rectangle')
        self.w = w
        self.h = h
    def area(self):
        a = self.w * self.h
        return a
class Circle(Shape):
    def __init__(self, r):
        super().__init__('Circle')
        self.r = r
    def area(self):
        a = math.pi * self.r**2
        return a
class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__('Triangle')
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        a = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        return a

r = Rectangle(20, 10)
a = r.area()
print(f"Area = {a:6.2f} {r}") # print(r) prints from the Shape

c = Circle(5)
a = c.area()
print(f"Area = {a:6.2f} {c}")

t = Triangle(5, 6, 7)
a = t.area()
print(f"Area = {a:6.2f} {t}")
