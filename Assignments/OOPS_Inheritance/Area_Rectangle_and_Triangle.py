#WAP to accept two numbers from the user and find area of rectangle and area of triangle

#Define class Shape
#Superclass - Animal
#Subclass - Rectangle
#Subclass - Triangle
class Shapes:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

#Define class Rectangle inheriting from Shape class
class Rectangle(Shapes):
    def rect(self):
        area=self.num1*self.num2
        return area

#Define class Triangle inheriting from Shape class
class Triangle(Shapes):
    def tri(self):
        area=0.5*self.num1*self.num2
        return area
        
print("Calculating the Area of Rectangle and Area of Triangle :")

#Taking input from user
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

#Creating the instance of child class
r=Rectangle(a,b)
t=Triangle(a,b)

#Calling class methods
#Printing the result
print("The Area of Rectangle is ",r.rect())
print("The Area of Triangle is ",t.tri())


