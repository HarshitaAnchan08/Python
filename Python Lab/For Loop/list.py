#Program to find the particular item is pesent in the list or not

#The below list contains integers, float, and strings.
list1=[10,10,20,"apple",34.5,"cherry","apple","apple"]

#Variable Initialization
search="apple"
count=0

#Print statements
print("The list is : ",list1)
print("Item to search is : ",search)

#for loop
for i in list1:
    if (i==search):
        count+=1   #count=count+1

#Conditional statement(if-else)
# the below if-else is used to count the no.of times item is present in the list.
if (count==0):
    print("Item not found in the list")
else:
    print("Item found in the list")
    print("Number of times of repeation of search item is : ",count)
