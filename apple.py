import math

class Apple:
    def __init__(self, color, shape, weight, size):
        self.color = color
        self.shape = shape
        self.weight = weight
        self.size = size

    def pluck_Apple(self):
        new_apple = self.weight - len(self.color)
        print("The {} apple plucked, has a value of {}.".format(self.color, new_apple))



apple = Apple("Green", "square", 20, "big")

apple.pluck_Apple()

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("The area of the circle is ", math.pi * (self.radius**2))


area = Circle(5)
area.area()
