#Basic proram to illustratethe use of constructor

#Define class
class Student:
    #Constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
 
#Define object      
p1=Student("John",36)

#Displaying output
print("My name is ",p1.name)
print("My age is ",p1.age)
