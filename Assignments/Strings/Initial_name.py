'''
Write a Python program to extract the initials from each student's name and create a new list of initials?(e.g., A.S for Alice Smith).
'''
def extract_initials(names):
    initials_list = []
    
    for name in names:
        # Split the name into parts
        parts = name.split()
        # Extract the first letter of each part and join them with a dot
        initials = '.'.join(part[0].upper() for part in parts) + '.'
        initials_list.append(initials)
    
    return initials_list

# Example list of student names
student_names = ["Devi Kapoor", "John Abhran", "Cindy June", "Lara lala"]

# Extract initials
initials = extract_initials(student_names)

# Print the result
print(initials)
