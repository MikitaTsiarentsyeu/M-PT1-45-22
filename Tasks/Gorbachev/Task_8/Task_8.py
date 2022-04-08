"""точка, отрезок, вектор, квадрат, прямоугольник, круг, эллипс"""
 
import math

class Point:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
       
    def set_x(self, x):
        self.__x = x
        
    def set_y(self, y):
        self.__y = y

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    
    def __str__(self) -> str:
        return f"coordinates x: {self.x}, y: {self.y}"  

p1 = Point(1, 3)
print(p1, '\n')

class SegmentV1: #aggregation
    
    def __init__(self, point_1, point_2) -> None:
        self.__point_1 = point_1
        self.__point_2 = point_2
    
    def __str__(self) -> str:
        return f"Point 1 {self.__point_1}; Point 2 {self.__point_2}"
    
   
class SegmentV2: #composition
    
    def __init__(self, x1, y1, x2, y2) -> None:
        self.point_1 = Point(x1, y1)
        self.point_2 = Point(x2, y2)
        self.len_p1_p2 = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
    
    def __str__(self) -> str:
        if self.len_p1_p2 == 0:
            return f'Segment is zero length (point) with {self.point_2}'
        else:
            return f"Segment: Point 1 {self.point_1}; Point 2 {self.point_2}. Length of segment is {self.len_p1_p2}"           
    

seg = SegmentV2(2,4,6,8)
print(seg, '\n')

seg1 = SegmentV2(2,4,2,4)
print(seg1, '\n')
   
class Vector(SegmentV2): 
       
    def __init__(self, x1, y1, x2, y2) -> None:
        super().__init__(x1, y1, x2, y2)
        self.coord_1 = int(x2) - int(x1)
        self.coord_2 = int(y2) - int(y1)
        
    def __str__(self) -> str:
        if self.coord_1 == self.coord_2 == 0:
            return f'This is the Zero Vector with point {self.point_1}'
        else:
            return f'Vector: Point 1 {self.point_1}; Point 2 {self.point_2}, Vector coordinates: ({self.coord_1}, {self.coord_2})'

vctr = Vector(1, 4, 5, 8)
print(vctr, '\n')

vctr1 = Vector(1, 4, 1, 4)
print(vctr1, '\n')

class Quadrilateral:
    
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4) -> None:
        """x1, y1 - first point of Quadrilateral,
            x2, y2 - second point of Quadrilateral,
            x3, y3 - third point of Quadrilateral,
            x4, y4 - fourth point of Quadrilateral,
        """
        self.__AB = Vector(x1, y1, x2, y2)
        self.__BC = Vector(x2, y2, x3, y3)
        self.__CD = Vector(x3, y3, x4, y4)
        self.__DA = Vector(x4, y4, x1, y1)
        self.__scal_mult_AB_BC = self.__AB.coord_1 * self.__BC.coord_1 + self.__AB.coord_2 * self.__BC.coord_2
        self.__scal_mult_BC_CD = self.__BC.coord_1 * self.__CD.coord_1 + self.__BC.coord_2 * self.__CD.coord_2
        self.__scal_mult_CD_DA = self.__CD.coord_1 * self.__DA.coord_1 + self.__CD.coord_2 * self.__DA.coord_2
        self.__scal_mult_DA_AB = self.__DA.coord_1 * self.__AB.coord_1 + self.__DA.coord_2 * self.__AB.coord_2
        self.__cos_AB_BC = self.__scal_mult_AB_BC / (self.__AB.len_p1_p2 * self.__BC.len_p1_p2)
        self.__cos_BC_CD = self.__scal_mult_BC_CD / (self.__BC.len_p1_p2 * self.__CD.len_p1_p2)
        self.__cos_CD_DA = self.__scal_mult_CD_DA / (self.__CD.len_p1_p2 * self.__DA.len_p1_p2)
        self.__cos_DA_AB = self.__scal_mult_DA_AB / (self.__DA.len_p1_p2 * self.__AB.len_p1_p2)
        
    def __str__(self) -> str:
        if (self.__cos_AB_BC == self.__cos_BC_CD == self.__cos_CD_DA == self.__cos_DA_AB == 0) and (self.__AB.len_p1_p2 == self.__BC.len_p1_p2 == self.__CD.len_p1_p2 == self.__DA.len_p1_p2): # this is square
            return f'Square sides: \nSegment AB {self.__AB},\nSegment BC {self.__BC},\nSegment CD {self.__CD},\nSegment DA {self.__DA}'
        elif (self.__cos_AB_BC != 0 or self.__cos_BC_CD != 0 or self.__cos_CD_DA != 0 or self.__cos_DA_AB != 0) and (self.__AB.len_p1_p2 == self.__BC.len_p1_p2 == self.__CD.len_p1_p2 == self.__DA.len_p1_p2): # this is square:
            return f'Rhombus sides: \nSegment AB {self.__AB},\nSegment BC {self.__BC},\nSegment CD {self.__CD},\nSegment DA {self.__DA}'
        elif (self.__cos_AB_BC == self.__cos_BC_CD == self.__cos_CD_DA == self.__cos_DA_AB == 0) and (self.__AB.len_p1_p2 != self.__BC.len_p1_p2 or self.__CD.len_p1_p2 != self.__DA.len_p1_p2): # this is rectangle:
            return f'Rectangle sides: \nSegment AB {self.__AB},\nSegment BC {self.__BC},\nSegment CD {self.__CD},\nSegment DA {self.__DA}'
        else:
            return f'This Quadrilateral is not correct!'
            
sqr = Quadrilateral(0, 2, 2, 0, 0, -2, -2, 0)  #square
print(sqr, '\n')  

sqr1 = Quadrilateral(0, 2, 1, 0, 0, -2, -1, 0)  #rhombus
print(sqr1, '\n')  

sqr2 = Quadrilateral(0, 0, 0, 2, 3, 2, 3, 0)  #rectangular
print(sqr2, '\n')  

sqr3 = Quadrilateral(10, 10, 0, 2, 3, 2, 3, 0)  #not correct rectangular
print(sqr3, '\n')  


class Circle(SegmentV2):
    
    def __init__(self, x, y, a, b) -> None:
        """ x and y - coordinates of point on circumference
        a, b - coordinates of center of circle
        """
        super().__init__(x, y, a, b)
        
    def __str__(self) -> str:
        if self.len_p1_p2 == 0:
            return f'This is a zero circle (point) with {self.point_2}'
        else:
            return f'Circle with center in point {self.point_2} with radius {self.len_p1_p2}'
        
crcl = Circle(1, 0, 0, 0)
print(crcl, '\n')

crcl1 = Circle(0, 0, 0, 0)
print(crcl1, '\n')

class Ellipse(SegmentV2):
    
    def __init__(self, x1, y1, x2, y2, a, b) -> None:
        """ x1 and y1 - coordinates of point on circumference
        x2, y2 - coordinates of center of ellipse
        a, b - semi-major and semi-minor axes
        """
        super().__init__(x1, y1, x2, y2)
        self.a = a
        self.b = b
        self.a_param = math.pow(self.a, 2)
        self.b_param = math.pow(self.b,2)
        self.ellips_param = math.pow(self.point_1.x - self.point_2.x, 2) / self.a_param + math.pow(self.point_1.y - self.point_2.y, 2)  / self.b_param
        
    def __str__(self) -> str:
        if self.ellips_param == 1 and self.a_param != self.b_param:
            return f'Ellipse with center point {self.point_2} and semi-major and semi-minor axes: {self.a}, {self.b}'
        elif self.ellips_param == 1 and self.a_param == self.b_param:
            return f'Circle with center in point {self.point_2} with radius {self.len_p1_p2}'
        elif self.len_p1_p2 == 0:
            return f'This is a zero ellipse (point) with {self.point_2}'
        else:
            return 'This is inccorect parameters for ellipse!'
    
ellps = Ellipse(0, -4 , 0, 0, 4, 7)
print(ellps, '\n')

ellps1 = Ellipse(0, 4 , 0, 0, 4, 4)
print(ellps1, '\n')

ellps2 = Ellipse(0, -4 , 0, 0, 16, 4)
print(ellps2, '\n')

ellps3 = Ellipse(0, 0, 0, 0, 16, 4)
print(ellps3, '\n')