#Program to print even numbers from 1 to 50

#Even numbers are numbers that get completely divisible by 2
#Initialize variables
add=0
num=1

print("Even numbers from 1 to 50 are : ")

#While loop
while num<=50:
    if (num%2==0):
        print(num)
        add+=num
    num+=1
#Printing sum result
print("\n Sum of even numbers from 1to 50 is : ",add)
