#WAP to find the second smallest element of  list

#empty list
list1=[]

#nmber of items in a list from user
n=int(input("Enter number of items in a list : "))

#taking numbers from user
for i in range(0,n):
    list1.append(int(input("Enter a number : ")))

#removing duplicates from the list
remove_dup=list(set(list1))

#sorting the list
sorted_list=sorted(remove_dup)

#print statements
print("The list is : ",list1)

#printing the second element of the sorted list
print("The second smallest number is : ",sorted_list[1])

