#Creating two classes with same method
#Method Overloading

#Class Rectangle
class Rectangle:
    def Area(self,leng,bre):
        a=leng*bre
        print("The Area of Rectangle is : ",a)
 
 #Class Square     
class Square:
    def Area(self,side):
        a=side*side
        print("The Area of Square is : ",a)

#creating instance for class Rectangle       
rect=Rectangle()
rect.Area(5,4)

#creatig instance for class Square
sq=Square()
sq.Area(3)
