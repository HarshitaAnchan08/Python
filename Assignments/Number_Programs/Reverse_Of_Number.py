#Program to find the Reverse of the entered number

#Taking num from user
num=int(input("Enter a number : "))

#Initialize the variables
rev=0
n=num

#Loop
#example-12345=>54321
#example2-345=>543
while n!=0:
    d=n%10
    rev=rev*10+d
    n//=10

#Print result
print("The Reverse of ",num," is : ",rev)
