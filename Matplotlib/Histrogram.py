#Histrogram

import numpy as np
import matplotlib.pyplot as plt

ages=np.random.normal(20,1.5,70)
print(ages)

plt.hist(ages)
