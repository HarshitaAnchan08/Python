#1st Pattern
#Program to print a Star Pattern

'''
*
* *
* * *
* * * *
'''
print("First Pattern")
#Number of rows
for i in range(1,5):
    #Number of columns
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print("\nSecond Pattern")

#2nd Pattern
#Program to print number pattern

'''
1
1 2
1 2 3
1 2 3 4
'''

#Number of rows
for i in range(1,5):
    #Number of Columns
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("\nThird Pattern")

#3rd Pattern
#Program to print number pattern

'''
1
2 2
3 3 3
4 4 4 4

'''

#Number of rows
for i in range(1,5):
    #Number of columns
    for j in range(i):
        print(i,end=" ")
    print()

