#Bar graph
#Number of students enrolled for particular courses

import numpy as np
import matplotlib.pyplot as plt

courses=["c","c#","python","data science","java"]
enrolled=[23,60,50,100,120]

plt.bar(courses,enrolled,color="green",width=0.3,edgecolor="black")
plt.show()
