from  abc import abstractmethod,ABC

from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#     def area(self):
#         return self.side * self.side
#
# def calculate_total_area(shapes):
#     return sum(shape.area() for shape in shapes)


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,high,width):
        self.__high=high
        self.__width=width
    def area(self):
        h=self.high
        w=self.width
        return h*w
    @property
    def high(self):
        return self.__high
    @high.setter
    def high(self,high):
        self.__high=self.__check_side(high)
    @high.getter
    def high(self):
        return self.__high
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        self.__width = self.__check_side(width)
    @width.getter
    def width(self):
        return self.__width
    def __check_side(side):
        if side<0:
            raise ValueError('Размер элемента фигуры некрекктен')
        else:
            return side

    def __str__(self):
        return f'Прямоугольник со сторонами {self.high}, {self.width} '

class Triangle(Shape):
    def __init__(self,high,tr_side):
        self.__high=high
        self.__tr_side=tr_side
    def area(self):
        return self.__high*self.tr_side*0.5
    @property
    def high(self):
        return self.__high
    @high.setter
    def high(self,high):
        self.__high=self.__check_side(high)

    @high.getter
    def high(self):
        return self.__high
    @property
    def tr_side(self):
        return self.__width
    @tr_side.setter
    def tr_side(self, tr_side):
        self.__width = self.__check_side(tr_side)

    @tr_side.getter
    def tr_side(self):
        return self.__tr_side
    def __check_side(side):
        if side<0:
            raise ValueError('Размер элемента фигуры некрекктен')
        else:
            return side

    def __str__(self):
        return f'Треугольник с высотокй {self.high} и основанием {self.tr_side}.'

rect=Rectangle(4,5)
triag=Triangle(10,6)
shapes=[rect,triag]
for shape in shapes:
    print(shape,'его площадь: ', shape.area())