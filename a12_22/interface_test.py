from abc import ABC, abstractmethod

# 定义一个抽象基类（接口）Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        """计算形状的面积"""
        pass

    @abstractmethod
    def perimeter(self):
        """计算形状的周长"""
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
