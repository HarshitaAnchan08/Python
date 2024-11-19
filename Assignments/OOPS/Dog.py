#Program to illustrate the use of OOPs.

#Define class
class Dog:
    #Define constructor
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    #Define methods
    def bark(self):
        print("The puppy is barking...")
        
    def dogInfo(self):
        print("The",self.name,"is",self.age,"years old.")
 
#Define object and calling object       
d=Dog("puppy",5)
d.bark()
d.dogInfo()
