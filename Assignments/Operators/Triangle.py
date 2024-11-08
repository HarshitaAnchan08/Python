#Importing Math module
import math
#Taking input from user
a=float(input("Enter first side : "))
b=float(input("Enter second side :" ))
c=float(input("Enter third side :" ))

#formulas
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
peri=a+b+c

#Printing result
print("Area of Triangle : ",area)
print("Perimeter of Triangle : ",peri)

