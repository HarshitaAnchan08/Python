#Program to check if the entered number is Palindrome Number or not

#Taking num from user
original_num=int(input("Enter a number : "))

#Initialize the variables
rev_num=0
n=original_num

#Loop
#example-12321
#example2-787
while n!=0:
    d=n%10
    rev_num=rev_num*10+d
    n//=10

#Print result
if original_num==rev_num:
    print(original_num," is a Palindrome Number")
else:
    print(original_num," is not a Palindrome Number")
