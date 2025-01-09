#Data Analysis of the weight of a person according to the each year

import numpy as np
import matplotlib.pyplot as plt

years = [2000 + x for x in range(10)]
weight = [80,34,78,67,78,38,29,67,67,67]

plt.plot(years,weight,c="g",lw=3,linestyle="-.")

plt.show()
