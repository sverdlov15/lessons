'''Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение
площади и периметра).
При потребности создавать все необходимые методы не описанные в задании. '''

import math

class Point:
    def __init__(self,  x: int, y: int):
        self.x = x
        self.y = y



class Figure:
    def __init__(self, circle: int, triangle: int, square: int):
        self.circle = circle
        self.triangle = triangle
        self.square = square


class Point(Circle):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius



class Point(Triangle):
    def area(self):
        return 0.5*b*c
    def perimetr(self):
        return c+d+e



class Point(Square)
    def area(self):
        return a**2
    def perimertr(self):
        return a*4









