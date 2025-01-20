#Program to check if the entered user number is Prime Number or not

#Taking num from user
num=int(input("Enter a number : "))

#Initialize the variables
is_prime=True

#Loop
#example-2,3,5,7,9,11,etc
if num<2:
    is_prime=False
else:
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break

#Print result
if is_prime:
    print(num," is Prime Number...")
else:
    print(num," is not Prime Number...")
