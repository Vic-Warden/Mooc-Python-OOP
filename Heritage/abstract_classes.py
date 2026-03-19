from abc import ABC, abstractmethod

# Abstract Parent Class
class Shape(ABC):
    
    # Method that MUST be overridden by children
    @abstractmethod
    def area(self):
        pass

# Child Class
class Square(Shape):
    def __init__(self, length):
        self.length = length

    # Overriding the parent's method
    def area(self):
        return self.length * self.length

# Instantiating the child class and calling
my_square = Square(5)
print(my_square.area())