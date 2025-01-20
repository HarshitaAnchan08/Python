#Program to find the Fibonacci Series of entered user number

#Taking input from user
num=int(input("Enter a number of series : "))

#Initialize the variables- a, b, add
a=0
b=1
add=0

#Printing the statement and value of a and b
print("The Fibonacci series of ",num," numbers is : ")
print(a)
print(b)

#Logical session
#adding a and b and storing in the add variable then printing it
#Then swapping the variables and continuing the loop
for i in range(1,num-1):
    add=a+b
    print(add)
    a=b
    b=add
