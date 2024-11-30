#WAP to find the last position of a given substring

#taking input from user- user_string and substring
user_string=input("Enter a string : ")
substring=input("Enter the substring to find : ")

#finding last position
last_pos=user_string.rfind(substring)

#checking if the substring is occurred in the user_string or not
if last_pos!=-1:
    print(f"The last occurrence of {substring} is at index : {last_pos}")
else:
    print(f"The substring {substring} is not founded in user string.")
