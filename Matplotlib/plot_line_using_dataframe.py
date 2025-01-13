import matplotlib.pyplot as plt
import pandas as pd

#data
data={
    "Cricket Bat":["SG","BOM","SS","GM","Spartan"],
    "MRP":[2000,2500,2700,6770,5000],
    "Weight_Grams":[1100,1200,1300,1000,1500]
}

#Dataframe
dataframe=pd.DataFrame(data)
#print(dataframe)

#plotting using pyplot.plot() method
#x and y co-ordinates from dataframe colums
plt.plot(dataframe["MRP"],dataframe["Weight_Grams"])

#display the figure
plt.show()
