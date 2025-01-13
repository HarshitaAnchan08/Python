#Plotting without lines
#Plotting with points

import matplotlib.pyplot as plt
import numpy as np

#x and co-ordinates
x_axis=np.array([3,4])
y_axis=np.array([2,9])

#plotting x and y co-ordinates
plt.plot(x_axis, y_axis,"o")

#display the graph
plt.show()
