#Program to print average of all numbers in a list

#create list
#list contain combination of data and it is mutable type
#Initialize empty list
list1=[]
#Initialize add variable
add=0

n=int(input("Enter number of elements for list : "))

#Entering user input in list
for i in range(0,n):
    list1.append(int(input("Enter elements : ")))
    
for i in list1:
    add=add+i
avg=add/n

print("The average of elements in a list are : ",avg)
