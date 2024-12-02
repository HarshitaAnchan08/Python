#List Comprehension2

#It is used to present list in concise and easy way
#As the size of code is decreased, the performance is increased

#Finding cube of even numbers

cube1=[]
for x in range(1,11):
    if(x%2==0):
        cube1.append(x**3)
print("Cube with normal for loop : ",cube1)


#Same code but with List Comprehension
cube2=[x**3 for x in range(1,11) if (x%2==0)]
print("Cube with list comprehension : ",cube2)
