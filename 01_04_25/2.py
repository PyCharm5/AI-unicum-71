import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Plane(Shape):
    @abstractmethod
    def perimeter(self):
        pass

class Volumetric(Shape):
    @abstractmethod
    def volume(self):
        pass

class Square(Plane):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2

    def perimeter(self):
        return self.a * 4

class Rectangle(Plane):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * self.a + 2 * self.b

class Circle(Plane):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

    def perimeter(self):
        return 2 * math.pi * self.radius

class Cube(Volumetric):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2 * 6

    def volume(self):
        return self.a ** 3

class Parallelepiped(Volumetric):
    def __init__(self, a, b ,c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return self.a * self.b * 2 + self.a * self.c * 2 + self.c * self.b * 2

    def volume(self):
        return self.a * self.b * self.c

class Ball(Volumetric):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 4 * math.pi * self.r**2

    def volume(self):
        return 4/3 * math.pi * self.r**3

class Pyramid(Volumetric):
    def __init__(self, s, h):
        self.s = s
        self.h = h

    def area(self):
        return self.s + 0.5 * self.s**0.5 * (self.h**2 + self.s**0.5*0.5)**0.5

    def volume(self):
        return self.s / 3 * self.h


class Formula(ABC):
    @abstractmethod
    def calculate(self):
        pass

class Discriminant(Formula):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate(self):
        D = self.b ** 2 - 4 * self.a * self.c
        x1 = (-self.b + D**0.5) / (2 * self.a)
        x2 = (-self.b - D ** 0.5) / (2 * self.a)
        return x1, x2

class Pythagoras(Formula):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        c = (self.a ** 2 + self.b ** 2) ** 0.5
        return c


class Factory:
    @staticmethod
    def create(type_, name, *args):
        if type_ == "shape":
             match name:
                case "square": return Square(args[0])
                case "rectangle": return Rectangle(args[0], args[1])
                case "circle": return Circle(args[0])
                case "cube": return Cube(args[0])
                case "parallelepiped": return Parallelepiped(args[0], args[1], args[2])
                case "ball": return Ball(args[0])
                case "pyramid": return Pyramid(args[0], args[1])


        elif type_ == "formula":
            match name:
                case "discriminant": return Discriminant(args[0], args[1], args[2])
                case "pythagoras": return Pythagoras(args[0], args[1])

        else:
            raise ValueError("Неизвестный команды")

user1 = Factory.create("shape", "cube", 5)