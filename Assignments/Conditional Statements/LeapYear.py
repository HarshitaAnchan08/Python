# Program to check if a year is a leap year or not

#Take user input
year=int(input("Enter a year : "))

#Logic Conditions
if((year%400==0) and (year%4==0 or year%100!=100)):
    print(year," is a Leap year.")
else:
    print(year," is not a Leap year.")

