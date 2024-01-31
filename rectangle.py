class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height  = height
    def getArea(self):
        return  self.width*self.height
    def getPerimeter(self):
        return (self.height + self.width)<<1
    def setHeight(self,height):
        self.height = height
    def setWidth(self,width):
        self.width = width

rec1 = Rectangle(2,2)
print(f"The area of rectangle is {rec1.getArea()}")
print(f"The perimeter of rectangle is {rec1.getPerimeter()}\n")

rec1.setHeight(3)
rec1.setWidth(3)

print(f"The area of rectangle is now {rec1.getArea()}")
print(f"The perimeter of rectangle is now {rec1.getPerimeter()}")
