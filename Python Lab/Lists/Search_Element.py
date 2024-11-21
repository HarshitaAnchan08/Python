#WAP to search a element in list and display proper result if found

#empty list
list1=[]

#number of items in a lit
n=int(input("Enter number of items in a list : "))

#taking input elements from user
for i in range(0,n):
    list1.append(input("Enter an element : "))

#taking input from user - element to search in a list
search=input("Enter an element to search : ")

#Initialize count variable
count=0

#iterating over each element in a list to find the search item 
for item in list1:
    if item==search:
        count+=1

#if count is greater than 0, then item found in a list    
if count>0:
    print(search,"element found in the list !!!")
    print("Number of occurrences of search item is : ",count)
else:
    print(search,"element not found in the list.")

