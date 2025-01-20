#Program to check if the entered year is Leap Year or not

#Taking year from user
year=int(input("Enter a number : "))

#example-2000,2004,2008,2012,etc
#Print result
if (year % 4 == 0 and year % 100 !=0) or (year % 400 ==0):
    print(year," is a Leap Year")
else:
    print(year," is not a Leap Year")
