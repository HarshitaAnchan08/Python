#Creating two classes with same method

#Class Vehicle
class Vehicle:
    def display(self):
        print("I have two wheeler")
 
 #Class Car      
class Car:
    def display(self):
        print("I have four wheeler")

#creating instance for class Vehicle       
veh=Vehicle()
veh.display()

#creatig instance for class Car
car=Car()
car.display()
