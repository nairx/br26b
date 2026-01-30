# Analyze and visualize a company’s monthly sales data using NumPy, 
# Pandas, and Matplotlib.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {
'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
'Sales': [25000, 27000, 30000, 28000, 35000, 37000, 40000, 42000, 41000, 45000, 47000, 50000]
}

df = pd.DataFrame(data)
print(df)

mean_sales = np.mean(df["Sales"])
highest_sales = np.max(df["Sales"])
lowest_sales = np.min(df["Sales"])
std_sales = np.std(df["Sales"])

print(f"Average Sales: {mean_sales}")
print(f"Highest Sales: {highest_sales}")
print(f"Lowest Sales: {lowest_sales}")
print(f"Standard Deviation: {std_sales}")

#Identify Best and Worst Month

best_month = df.loc[df["Sales"].idxmax(),"Month"]
print(best_month)
best_month = df.loc[df["Sales"].idxmin(),"Month"]
print(best_month)

plt.plot(df["Month"],df["Sales"])
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Sales Trend")
plt.savefig("salesreport.png")
plt.show()