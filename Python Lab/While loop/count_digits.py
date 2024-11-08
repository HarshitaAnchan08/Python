#Program to count number of digits in a given number

#Input number from user
num=int(input("Enter a number : "))
n=num

#count variable
count=0

#Loop
#Logic to count digits in a number
while(num!=0):
    rem=num%10
    count+=1
    num//=10

#Printing result
print("The number of digits in",n," is : ",count)

