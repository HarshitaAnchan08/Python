#Program to Factorial of a number

#Initialize fact variable
fact=1

#Taking input from user
num=int(input("Enter a number : "))

for i in range(1,num+1):
    #Printing result
    fact*=i

#Printing factorial result
print("The factorial of ",num," is : ",fact)
