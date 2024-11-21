#WAP to remove duplicate elements from a list and sort the element

#empty list
mylist=[]

#number of items in a list
n=int(input("Enter number of items for list : "))

#taking input from user
for i in range(0,n):
    mylist.append(input("Enter a element : "))

#print statements
#printing orginal list
print("\nThe orginal list is : ",mylist)

#printing after removing duplicate items
remove_dup=list(set(mylist))
print("Printing list after removing the duplicate elements : ",remove_dup)

#printing after sorting items
sorted_list1=sorted(mylist)
print("Printing list after sorting : ",sorted_list1)

#printing after both sorting and removing duplicates
sorted_list2=sorted(remove_dup)
print("Printing list after both sorting and removing duplicates : ",sorted_list2)
