#Initialize reverse(rev) variable with 0
rev=0

#Taking input from user
num=int(input("Enter a number : "))
n=num

#While loop
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n//=10
    
#Printing result
print("The reverse of ",num," is : ",rev)
