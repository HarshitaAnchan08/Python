#Initialize count variable with 0
count=0

#Taking input from user
num=int(input("Enter a number : "))
n=num

#While loop
while n!=0:
    rem=n%10
    count+=1
    n//=10
    
#Printing result
print("The Number of digits in ",num," is : ",count)
