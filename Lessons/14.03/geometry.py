class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y
    
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    x = property(get_x, set_x)
    y = property(get_y, set_y)

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

p1 = Point(2, 4)
p2 = Point(3, 6)
print(p1, p2)

class SegmentV1: #aggregation

    def __init__(self, point_1, point_2) -> None:
        self.__point_1 = point_1
        self.__point_2 = point_2

    def __str__(self) -> str:
        return f"Point 1: {self.__point_1}; Point 2: {self.__point_2}"

s = SegmentV1(p1, p2)
print(s)

class SegmentV2: #composition

    def __init__(self, x1, y1, x2, y2) -> None:
        self.__point_1 = Point(x1, y1)
        self.__point_2 = Point(x2, y2)

    def __str__(self) -> str:
        return f"Point 1: {self.__point_1}; Point 2: {self.__point_2}"

s = SegmentV2(3,5,7,9)
print(s)