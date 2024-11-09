#Program to check if the user given number is palindrome or not

#Example- 121, 1234321, 787

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

#if original number is equal to reverse of a number then it is palindrome number
if (num==rev):
    print(num, " is a Palindrome number.")
else:
    print(num," is not a Palindrome number.")
