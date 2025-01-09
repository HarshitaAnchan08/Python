#Pie Chart
#Pie Chart for the number of people enrolled for the paticular course

import numpy as np
import matplotlib.pyplot as plt

courses=["c","c#","python","data science","java"]
enrolled=[23,60,50,100,120]

plt.pie(enrolled,labels=courses)

plt.show()
