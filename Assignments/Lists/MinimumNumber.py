#Program to print minimum number in a list

#create list
#list contain combination of data and it is mutable type
#Initialize empty list
list1=[]

n=int(input("Enter number of elements for list : "))
for i in range(0,n):
    num=int(input("Enter a number : "))
    list1.append(num)
    
if list1:
    min=list1[0]
    if i<min:
        min=i
    print("Minimum number is : ",min)
else:
    print("List is empty.")
