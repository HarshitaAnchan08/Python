#Program to check if the entered user number is Armstrong Number or not

#Taking num from user
original_num=int(input("Enter a number : "))

#Initialize the variables
add=0
n=original_num
num_digit=len(str(original_num))

#Loop
#example-153=1+125+27=153
#example2-1634=1+1296+27+26
while n!=0:
    d=n%10
    add=add+d**num_digit
    n//=10

#Print result
if original_num==add:
    print(original_num," is an Armstrong Number...")
else:
    print(original_num," is not an Armstrong Number...")

