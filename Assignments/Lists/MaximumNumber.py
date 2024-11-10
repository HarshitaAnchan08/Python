#Program to print maximum number in a list

#create list
#list contain combination of data and it is mutable type
#Initialize empty list
list1=[]

n=int(input("Enter number of elements for list : "))

#Taking user input for list
for i in range(0,n):
    num=int(input("Enter number : "))
    list1.append(num)
 
#findig maximum number   
if list1:
    max=list1[0]
    for i in list1:
        if i>max:
            max=i;
    print("Maximum number is : ",max)
else:
    print("List is empty.")
