#Program to find the Sum Of Digits of the entered number

#Taking num from user
num=int(input("Enter a number : "))

#Initialize the variables
add=0
n=num

#Loop
#example-12345=1+2+3+4+5=15
while n!=0:
    d=n%10
    add+=d
    n//=10

#Print result
print("The Sum Of Digits of ",num," is : ",add)
