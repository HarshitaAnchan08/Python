#Program to check if a person can vote or not using function

#Taking input from user
age=int(input("Enter your age : "))

#A person can vote only if the person is equal or greater than 18
#Function definition
def vote(age):
    if(age>=18):
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
        
#Calling Function
vote(age)
