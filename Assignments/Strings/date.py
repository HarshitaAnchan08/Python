'''
Develop a Python script that converts a date from "MM/DD/YYYY" format to "DD MonthName YYYY" format.
For example:
Input: "05/21/2023"
Output: 21 May 2023
'''
from datetime import datetime

def convert_date_format(date_str):
    # Parse the input date string
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    
    # Format the date in "DD MonthName YYYY" format
    formatted_date = date_obj.strftime("%d %B %Y")
    
    return formatted_date

# Example input
input_date = "05/21/2023"
output_date = convert_date_format(input_date)

# Print the output
print(input_date)
print(output_date)

text = "Python is fun!"
corrected_text = text.replace('Python', 'Java')
print(corrected_text)



