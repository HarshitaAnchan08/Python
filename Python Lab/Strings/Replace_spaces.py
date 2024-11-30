#WAP to accept a string replace all spaces by Hash(#) symbol.

#creating function to replace all spaces by hash(#)
def Replace_Spaces(user_string):

    #replacing spaces by #
    new_string=user_string.replace(" ","#")
    print("The replaced string is : ",new_string)

#taking input string from user
user_string=input("Enter a string : ")

#calling function
Replace_Spaces(user_string)
