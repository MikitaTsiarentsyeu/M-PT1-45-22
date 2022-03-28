from math import *


class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return f"x: {self.x}, y:{self.y}"

    x = property(get_x, set_x)
    y = property(get_y, set_y)


p1 = Point(2, 4)
p2 = Point(5, 7)
print(p1, p2)


class SegmentV1:  # AGGREGATION

    def __init__(self, point_1, point_2):
        self.__point1 = point_1
        self.__point2 = point_2

    def __str__(self):
        return f"Point_1 : {self.__point1}, Point_2 : {self.__point2}"


s1 = SegmentV1(p1, p2)
print(p1, p2)


class SegmentV2:  # COMPOSITION

    def __init__(self, x1, y1, x2, y2):
        self.__point1 = Point(x1, y1)
        self.__point2 = Point(x2, y2)

    def __str__(self):
        return f"Point_1 : {self.__point1}, Point_2 : {self.__point2}"


s2 = SegmentV2(1, 5, 4, 8)
print(s2)


class Vector:

    def __init__(self, x1, x2, y1, y2, alpha):
        self.__point1 = Point(x1, y1)
        self.__point2 = Point(x2, y2)
        self.__alpha = alpha

    def __str__(self):
        return f"Point_1: {self.__point1}; Point_2: {self.__point2}; Alpha: {self.__alpha}"


vec = Vector(2, 3, 5, 4, 1.2)
print(vec)


class Square:

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.__x1 = x1
        self.__x2 = x2
        self.__x3 = x3
        self.__x4 = x4
        self.__y1 = y1
        self.__y2 = y2
        self.__y3 = y3
        self.__y4 = y4
        self.__point1 = Point(x1, y1)
        self.__point2 = Point(x2, y2)
        self.__point3 = Point(x3, y3)
        self.__point4 = Point(x4, y4)

    def isSquare(self):
        if (self.__x2 - self.__x1) == (self.__x3 - self.__x4) == (self.__y1 - self.__y4) == (self.__y2 - self.__y3):
            return True
        else:
            return False

    def __str__(self):
        if self.isSquare():
            return f"Yes, it is square with points: p1 = {self.__point1}, p2 = {self.__point2}, p3 = {self.__point3}, p4 = {self.__point4}"
        else:
            return "No, it is not square"


square = Square(2, 5, 5, 5, 5, 2, 2, 2)
a = square.__str__()
print(a)


class Rectangle:

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.__x1 = x1
        self.__x2 = x2
        self.__x3 = x3
        self.__x4 = x4
        self.__y1 = y1
        self.__y2 = y2
        self.__y3 = y3
        self.__y4 = y4
        self.__point1 = Point(x1, y1)
        self.__point2 = Point(x2, y2)
        self.__point3 = Point(x3, y3)
        self.__point4 = Point(x4, y4)

    def isRectangle(self):
        if (self.__x2 - self.__x1) == (self.__x3 - self.__x4) and (self.__y1 - self.__y4) == (self.__y2 - self.__y3):
            if (self.__x2 - self.__x1) == (self.__x3 - self.__x4) == (self.__y1 - self.__y4) == (self.__y2 - self.__y3):
                return f"No, it is square"
            else:
                return f"Yes, it is rectangle with points: p1 = {self.__point1}, p2 = {self.__point2}, p3 = {self.__point3}, p4 = {self.__point4}"
        else:
            return "No, it is not rectangle"


rectangle = Rectangle(3, 8, 7, 8, 7, 2, 3, 2)
a = rectangle.isRectangle()
print(a)


class Circle:

    def __init__(self, x, y, r):
        self.__x = x
        self.__y = y
        self.__r = r

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_r(self, r):
        self.__r = r

    def get_r(self):
        return self.__r

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    r = property(get_r, set_r)

    def isCircle(self):
        if pow(self.__x, 2) + pow(self.__y, 2) == round(pow(self.__r, 2), 2):
            return f"Yes it is circle with radius: {self.__r}"
        else:
            return "No, it is not circle"


#ENTER BORDER POINTS OF CIRCLE (x = 3, y = 0)
circle = Circle(1, 0, 1)
print(circle.isCircle())
