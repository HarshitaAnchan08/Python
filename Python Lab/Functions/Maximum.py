#Program to find maximum among two numbers using function

#Taking input from user
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))

#Function definition
def maximum(a,b):
    if (a>b):
        return a
    else:
        return b
        
#Calling Function
maximum_res=maximum(num1,num2)
print("The maximum number is : ",maximum_res)


