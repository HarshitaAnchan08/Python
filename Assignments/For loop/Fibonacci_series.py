#Program to find fibonacci series

#Initialize fact variable
n1=0
n2=1
add=0

#Taking input from user
series=int(input("Enter a number : "))

#Print statement
print("The fibonacci series for ",series," are : ")

#Printing n1 and n2 variables
print(n1)
print(n2)

#for loop
for i in range(0,series-2):
    add=n1+n2
    print(add)
    n1=n2
    n2=add
