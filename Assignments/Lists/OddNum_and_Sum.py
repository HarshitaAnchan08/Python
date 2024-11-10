#Program to print odd numbers and print sum of all odd numbers in a list

#create list
#list contain combination of data and it is mutable type
list1=[1,33,4,33,89,75,88,90]

#Initialize add variable
add=0

print("Odd numbers in a list are : ")
for num in list1:
    if (num%2!=0):
        print(num)
        add+=num  #add=add+num

#Printing Sum of odd numbers from list        
print("The sum of all odd numbers in the list is : ",add)
