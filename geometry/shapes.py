import math


class Shape:
    def area(self):
        raise NotImplementedError("Надо переопределить area()")


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        # простая валидация — чтобы не городить фигню
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("Стороны должны быть положительными")

        # проверка существования треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Такой треугольник не существует")

        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Формула Герона
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self):
        # Проверка по теореме Пифагора
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
