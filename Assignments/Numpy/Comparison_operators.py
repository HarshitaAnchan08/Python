#imporing numpy module
import numpy as np

#creating two arrays
a=np.array([101,99,87])
b=np.array([897,97,111])

#printing arrays
print("Array a : ",a)
print("Array b : ",b)

#operators- >,>=,<,<=
print("a>b")
print(np.greater(a,b))

print("a>=b")
print(np.greater_equal(a,b))

print("a<b")
print(np.less(a,b))

print("a<=b")
print(np.less_equal(a,b))
