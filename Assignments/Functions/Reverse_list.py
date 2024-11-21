#WAP to reverse a list with function without using reverse function

#Function definition
def reverse(mylist):
    return l[::-1]
    
#l=[67,76,89,90,100]
#Empty list
l=[]
#Taking number of items in list
n=int(input("Enter number of elements for list : "))

#Taking input from user 
for i in range(0,n):
    l.append(int(input("Enter element : ")))
    
#Printing orginal list
print("The original list is : ",l)

#Calling function def
res=reverse(l)

#Printing reversed list
print("The reverse of list is : ",res)
