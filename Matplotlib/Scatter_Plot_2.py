#Scatter plotting with random generated numbers

import numpy as np
import matplotlib.pyplot as plt

x_data=np.random.random(100)*100
y_data=np.random.random(100)*100

plt.scatter(x_data,y_data,color='green',s=150,marker='D',alpha=0.3)
plt.show()
