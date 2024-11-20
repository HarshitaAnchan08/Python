#Password Generator in python

#Importing random module
import random

#Storing all charcaters in chars variable
chars="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"

#Print statement
print("---Password Generator---")

#Taking length of password from user
length=int(input("Enter length for password : "))

#Initialize password variable
password=""

#Loop condition
#logic
for i in range(length):
    password+=random.choice(chars)
    
#Printing the generated password
print("The Generated password is : ",password)
