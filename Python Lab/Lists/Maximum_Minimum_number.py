#WAP to find minimum and maximum element in a list

#empty list
mylist=[]

#asking user for number of items in a list
n=int(input("Enter number of items for list : "))

#taking elements from user
for i in range(0,n):
    mylist.append(int(input("Enter a number : ")))

#intialize the variable
max_num=mylist[0]
min_num=mylist[0]

#loop for conditions and logic
for i in mylist:
    #maximum number
    if i>max_num:
        max_num=i

    #minimum number
    if i<min_num:
        min_num=i

#print statements
print("The list is : ",mylist)
print("Maximum number is : ",max_num)
print("Minimum number is : ",min_num)
                  
