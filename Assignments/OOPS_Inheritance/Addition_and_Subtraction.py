#WAP to find addition and subtration using inheritance concept

#Define clas Operations
class Operations:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

#Define child class Addition
class Addition(Operations):
    def add(self):
        print("The addition is ",self.num1+self.num2)
        
#Define cild class Subtraction
class Subtraction(Operations):
    def sub(self):
        print("The subtraction is ",self.num1-self.num2)
        
#Instance of child classes
a=Addition(34,6)
s=Subtraction(22,10)

#Calling class methods
a.add()
s.sub()
