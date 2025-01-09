#Scatter Plot
#Scatter plot with random numbers and star marker

import numpy as np
import matplotlib.pyplot as plt

x_data=np.random.random(50)*100
y_data=np.random.random(50)*100

plt.scatter(x_data,y_data,color="green",s=150,marker="*")
plt.show()
