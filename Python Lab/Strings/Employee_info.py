#WAP to get employee information to store his official information (eid, designation)

#Defining class
class Employee:

    #Constructor
    def __init__(self,eid,desgn):
        self.eid=eid
        self.desgn=desgn
    #method with no parameters
    def store_info(self):
        print("Employee ID is : ",self.eid)
        print("Employee Designation is : ",self.desgn)

#taking input from user
emp_eid=int(input("Enter EID : "))
emp_desgn=input("Enter Designation : ")

#creating object
e1=Employee(emp_eid,emp_desgn)

#calling class method
print("\nStored Employee Information : ")
e1.store_info()
