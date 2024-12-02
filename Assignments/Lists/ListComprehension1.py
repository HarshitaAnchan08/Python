#List Comprehension

#It is used to present list in concise and easy way
#As the size of code is decreased, the performance is increased

marks=[20,30,40,50,60]
new_marks=[]     #Empty List
for x in marks:
    new_marks.append(x+2)
print("New marks are : ",new_marks)


#Same code but with List Comprehension
marks=[20,30,40,50,60]
new_marks=[x+2 for x in marks]
print("New marks are with list comprehension : ",new_marks)
