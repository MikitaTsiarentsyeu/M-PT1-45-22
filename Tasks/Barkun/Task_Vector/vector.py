class Vector:
   
    def __init__ (self, x, y):                               #инициализирование атрибутов класса Vector
        self.x = x
        self.y = y
    
    def __str__(self):                                      #приведение к строковому виду
        return f'class Vector [{self.x}, {self.y}]'

    # def __repr__(self):                         
    #     return f'[{self.x}, {self.y}]'          
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
 
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
 
    def __mul__(self, a):
        return Vector(self.x * a, self.y * a)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
        
 
vct1 = Vector(5, 10)
vct2 = Vector(15, 25)
vct3 = Vector(-3, -7)
a = 3
print(f'\n {vct1} {vct2} {vct3} {type(vct3)}')
print(f'\nСложение вектров V1 + V2 + V3: {vct1 + vct2 + vct3}')
print(f'\nРазность вектров V1 - V3: {vct2 - vct3}')
print(f'\nСкалярное произведение вектора V2  на число 3: {vct2 * a}')
print(f'\nДлина вектора V1: {round(abs(vct1), 2)}\n')

