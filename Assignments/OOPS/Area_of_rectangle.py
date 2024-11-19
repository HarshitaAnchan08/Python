#Program to find Area of rectangle using OOPs.

#Define class
class Rectangle:
    #Define constructor
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    #Define methods
    def rect(self):
        res=self.l*self.b
        return res

#Taking input from user
leng=int(input("Enter length : "))
bre=int(input("Enter breadth : "))

#Define instance of the class Rectangle      
obj=Rectangle(leng,bre)
ans=obj.rect()
print("The Area of rectangle is : ",ans)
