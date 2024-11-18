#Program to find addition of two numbers using OOPS concept

#Define class
class Test:
    #Define method
    def add(self,a,b):
        res=a+b
        return res

#Taking input from users
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

#Define object
obj=Test()

#Storing add method result in ans variable
ans=obj.add(a,b)

#Displaying output
print(f"The addition of {a} and {b} is : ",ans)
