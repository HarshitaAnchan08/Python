#WAP to Reverse a string

#creating a function to reverse a string
def Reverse_String(user_string):
    
    #storing the string in reverse order
    rev_string=user_string[::-1]

    #printing result
    print(f"The Reverse of {user_string} is : {rev_string}")

#taking string from user    
user_string=input("Enter a string : ")

#calling function with parameter
Reverse_String(user_string)
