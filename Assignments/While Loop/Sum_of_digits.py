#Initialize add variable with 0
add=0

#Taking input from user
num=int(input("Enter a number : "))
n=num

#While loop
while n!=0:
    rem=n%10
    add+=rem
    n//=10
    
#Printing result
print("The sum of digits of ",num," is : ",add)
