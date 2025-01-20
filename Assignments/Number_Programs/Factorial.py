#Program to find the Factorial of entered user number

#Taking num from user
num=int(input("Enter a number : "))

#Initialize the fact variable
fact=1

#Loop
#example-5!=5*4*3*2*1=120
for i in range(1,num+1):
    fact*=i

#Print result
print("The Factorial of ",num," is : ",fact)
