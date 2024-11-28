'''
Imagine you're an assistant managing an event guest list. You have a string containing names and email addresses separated by semicolons, as shown below:"

guests = "Alice Smith<alice@example.com>; Bob Stone<bob@example.com>; Cara Wins<cara@example.com>"

Can you extract and print each guest's name separately from their email?
'''
guests = "Alice Smith<alice@example.com>; Bob Stone<bob@example.com>; Cara Wins<cara@example.com>"
#separating colons
guest_list=guests.split(';')

#running loops to separate guest name from string
for guest in guest_list:
    name_email = guest.strip().split('<')
    name = name_email[0].strip() 
    email = name_email[1].strip('>') 
    
    print(f"Guest name : {name}, Email : {email}")
    
