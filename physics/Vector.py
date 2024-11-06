import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)
    
    def subtract(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)
    
    def scale(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
