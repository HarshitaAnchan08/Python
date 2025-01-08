import matplotlib.pyplot as plt

#Sample data
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
avg_temperatures=[5,7,10,13,17,20,23,22,19,14,9,6]

#Create bar chart
plt.figure(figsize=(10,6))
plt.bar(months, avg_temperatures, color='skyblue')

#Add labels and titles
plt.title("Average Monthy Temperatures ",fontsize=16)
plt.xlabel("Month ",fontsize=12)
plt.ylabel("Temperature ( C) ",fontsize=12)

#Show gridlines for better readability
plt.grid(axis="y", linestyle="--", alpha=0.5)

#Display the chart
plt.show()

