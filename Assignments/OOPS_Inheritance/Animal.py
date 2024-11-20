#Program to illustrate the use of OOPs Inheritance.

#Define parent class
class Animal:
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        return f"{self.name} barks"
        
#Class Dog inheriting from Animal class    
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

#Class Cat inheriting from Cat class        
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"
        
#Creating instance of the class
dog=Dog("Buddy")
cat=Cat("Whiskers")

#Calling the Methods
print(dog.speak())
print(cat.speak())


