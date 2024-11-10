#Program to get the factorial of a number using function

#Taking input from user
num=int(input("Enter a number : "))

#Function definition
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
    
#Calling Function
factorial_res=factorial(num)
print("The Factorial of ",num," is : ",factorial_res)

'''
Example
Fcatorial of 5 is 120
5*4*3*2*1=120
'''
