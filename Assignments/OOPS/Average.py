#Program to find average of three numbers using OOPs.

#Define class
class Average:
    #Define method
    def avg(self,n1,n2,n3):
        add=n1+n2+n3
        res=add/3
        return res
 
#Taking input from user      
n1=int(input("Enter first number : "))
n2=int(input("Enter second number : "))
n3=int(input("Enter third number : "))

#Define object
A=Average()

#Storing result in res variable
res=A.avg(n1,n2,n3)

#Printing output
print("The average of three numbers is : ",res)
