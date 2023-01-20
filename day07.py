# day07

import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        print('도형의 면적을 출력합니다.')


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, x, y, width, length):
        super(Rectangle, self).__init__(x, y)
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

class Cylinder(Circle):
    def __init__(self, x, y, radius, height):
        super().__init__(x, y, radius)
        self.radius = radius
        self.height = height

    def get_area(self):
        return super().get_area() * self.height
#        return math.pi * (self.radius ** 2) * self.height


c1 = Circle(100, 100, 10.0)
c2 = Circle(50, 50, 2.0)
r1 = Rectangle(100, 50, 5, 2)
cy1 = Cylinder(20, 20, 10.0, 2)

print(f'사각형의 좌표는 x: {r1.x}, y: {r1.y}이고 넓이는 {r1.get_area()}입니다.')
print(f'원의 좌표는 x: {c2.x}, y: {c2.y}이고 넓이는 {c2.get_area()}입니다.')
print(f'원의 좌표는 x: {c1.x}, y: {c1.y}이고 넓이는 {c1.get_area()}입니다.')
print(f'원기둥의 좌표는 x: {cy1.x}, y: {cy1.y}이고 넓이는 {cy1.get_area()}입니다.')

