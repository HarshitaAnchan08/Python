#Strong Password Generator

#The password will include atleast one number, one uppercase letter, one special character and remaining lowercase letters.

#Importing random module
import random

#String containing all possibilities
sp_chars="!@#$%^&*()"
numbs="0123456789"
upp_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_chars="abcdefghijklmnopqrstuvwyz"

#Initializing variable
password=""
low_ch=""

#Storing random characters into the variable
sp_ch=random.choice(sp_chars)
num=random.choice(numbs)
upp_ch=random.choice(upp_chars)

#Print statement
print("---Strong Password Generator---")

#Taking length from user
length=int(input("Enter length of password : "))

#Length must be greater or equal to 8
if length>=8:
    for i in range(length-3):
        low_ch+=random.choice(low_chars)
    password=upp_ch+sp_ch+low_ch+num
    
    #Converting string into list for random shuffling
    password_list=list(password)
    random.shuffle(password_list)
    
    #Converting list back to string
    strong_password=''.join(password_list)
    print("The Generated strong password is : ",strong_password)
else:
    print("The password atleast should be 8 characters long")
