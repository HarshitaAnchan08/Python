#Program to print even numbers and print sum of all even numbers in a list

#create list
#list contain combination of data and it is mutable type
list1=[1,33,4,89,56,87,98,34]

#Initialize add variable
add=0

print("Even numbers in a list are : ")
for num in list1:
    if (num%2==0):
        print(num)
        add+=num  #add=add+num

#Printing Sum of even numbers from list        
print("The sum of all even numbers in the list is : ",add)
