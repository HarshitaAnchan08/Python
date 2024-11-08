#Program to get Factorial of positive number

#Initialization
fact=1
i=1

#Input positive number from user
num=int(input("Enter a positive number : "))

#while loop
#num=4
#4*3*2*1=24
while (i<=num):
    fact=fact*i
    i+=1

#Printing result
print("The Factorial of ",num," is : ",fact)

'''
4!=4*3*2*1

Iteration 1: num=4
            1<=4
            fact=1*1
            i=i+1

Iteration 2: num4
            2<=4
            fact=1*2
            i=i+1

Iteration 3: num=4
            3<=4
            fact=2*3
            i=i+1

Iteration 4: num=4
            4<=4
            fact=6*4
            i=i+1

Hence when condition becomes false, the factorial of 4 will be 24.
'''

            
            
