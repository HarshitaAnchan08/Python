#Imprting numpy module
import numpy as np

#creating array from list
a=[1,3,4,5,66]
arr=np.array(a)
print(arr)

#changing number at index 2
a[2]=27
print(a)

#One dimensional array with only zeros
a=np.zeros(5,dtype=int)
print(a)

#Two dimensional array with only zeros
b=np.zeros([2,3],dtype=int)
print(b)

#Two dimensional number array
c=np.array([[1,2,3],[4,5,6],[6,4,2]])
print(c)

#printing type of array c
print(c.dtype)

#printing array shape/size
print(c.shape)

#One dimensional array with only ones
a=np.ones(5,dtype=int)
print(a)

#Two dimensional array with only ones
b=np.ones([2,3],dtype=int)
print(b)
