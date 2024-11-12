class Rectangle:
    def __init__(self, length, width):   # Constructor
        self.length = length
        self.width = width
    
    def area(self):  # Class Function
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width
    
    
length = int(input("Enter Length: "))
width  = int(input("Enter Width: "))
r = Rectangle(length, width)  # Call class instructor to make new instance
print("Area: ", r.area())
print("Perimeter: ", r.perimeter())
r.length *= 2
print("Length * 2: ", r.length)
    
input()