#Program to print odd numbers from 1 to 50

#Odd numbers are numbers that does not get completely divisible by 2
#Initialize variables
add=0
num=1

print("Odd numbers from 1 to 50 are : ")

#While loop
while num<=50:
    if (num%2!=0):
        print(num)
        add+=num
    num+=1

#Printing sum result
print("\n Sum of odd numbers from 1to 50 is : ",add)
