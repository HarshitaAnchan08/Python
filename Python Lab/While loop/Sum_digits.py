#Program to calculate sum of digits of a number

#total variable
total=0

#Taking Input from user
num=int(input("Enter a number : "))
n=num

#Loop
#Logical section
while (n!=0):
    rem=n%10
    total+=rem
    n//=10

#Printing statement
print("The sum of all digits in ",num," is : ",total)

'''
example
num=12345
total=15

output: Sum of digits of 12345 is 15
'''
