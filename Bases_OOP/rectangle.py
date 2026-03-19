# Exemple : Declaration of a class with attributes and methods
class RectangleSimple:
    width = 3
    height = 2

    def calculate_area(self):
        return self.width * self.height


# Exemple : Declaration of a class with attributes and methods, including a constructor
class Rectangle:
    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color
        
    # Example of a method that does not return anything (void method)
    def empty_method(self, length):
        pass