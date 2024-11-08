#Functions are reusable blocks of code
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
#define function
def addition(a,b):
    res=a+b
    print("The Addition of two numbers is : ",res)
    
#calling function
addition(num1,num2)
addition(5,8)

#Use of return statement
def addition(a,b,c):
    res=a+b+c
    return res
    
total_sum=addition(5,3,2)
print("The Addition of three numbers is : ",total_sum)
