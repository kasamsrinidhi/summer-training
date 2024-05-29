class Shape(metaclass=ABCMeta):
    def __init__(self):
        print("iam init")
    def draw_shape(self):
        pass
    def set_color(self):
        pass
class Circle(Shape):
    def draw_shape(self):
        print("draw circle")
#o/p-cant implement set_color()method

        