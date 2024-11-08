#Program to prit fibonacci series up to n terms

#Taking number of terms from user
n=int(input("Enter number of terms : "))

#Initialization
n1=0
n2=1
total=0
cnt=1

print("The Fibonacci series for ",n," terms are :")

#Prnting variable n1 and n2
print(n1)
print(n2)

#Loop
#Logical section
while(cnt<=n-2):
    total=n1+n2
    print(total)
    n1=n2
    n2=total
    cnt+=1
