#Program to print table of a number using function

#Taking input from user
num=int(input("Enter a number : "))

#Function definition
def table(n):
    print("\nThe table of ",n," is : ")
    for i in range(1,11):
        print(num," X ",i," = ",n*i)
        
#Calling Function
table(num)

