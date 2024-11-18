#Program for Arithmetic operations of two numbers using OOPS concept

#Define class
class Test:
    #Define method
    #addition
    def add(self,a,b):
        res=a+b
        return res
        
    #subtraction
    def sub(self,a,b):
        res=a-b
        return res
    
    #multiplication
    def multi(self,a,b):
        res=a*b
        return res
      
    #division 
    def div(self,a,b):
        res=a/b
        return res

#Taking input from users
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

#Define object
obj=Test()

#Storing add method result in ans variable
ans1=obj.add(a,b)
ans2=obj.sub(a,b)
ans3=obj.multi(a,b)
ans4=obj.div(a,b)

#Displaying output
print(f"\nThe addition of {a} and {b} is : ",ans1)
print(f"The subtraction of {a} and {b} is : ",ans2)
print(f"The multipliation of {a} and {b} is : ",ans3)
print(f"The division of {a} and {b} is : ",ans4)


