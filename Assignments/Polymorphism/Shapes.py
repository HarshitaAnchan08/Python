#Polymorphism

class Shape:
    def Area(self):
        pass   #This is a placeholder for a method to be overridden
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def area(self):
        return self.length*self.width
        
class Square(Shape):
    def __init__(self,side):
        self.side=side
        
    def area(self):
        return self.side*self.side

#Function to calculate area using polymorphism        
def calculate_area(Shape):
    return Shape.area()
    
#Create instance of Rectangle an Square
rectangle=Rectangle(10,5)
square=Square(4)

#calculate and print areas
print("Area of Rectangle : ",calculate_area(rectangle))
print("Area of Square : ",calculate_area(square))


