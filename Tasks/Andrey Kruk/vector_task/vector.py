# задание к следующему занятию - для класса Вектор реализовать методы для сложения,
# разности, умножения на скаляр и вычисления длины (всё через стандартные операторы/функции)

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector(self.x * scalar, self.y * scalar)
        raise ValueError('Can only multiply by a scalar')

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"{self.x}, {self.y}"

v1 = Vector(1,2)
v2 = Vector(3,4)

print(v1)
print(v1 + v2)
print(v1 - v2)
print(v1 * 5)
print(abs(v1))


