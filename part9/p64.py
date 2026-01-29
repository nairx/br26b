import matplotlib.pyplot as plt
year = ["2021","2022","2023","2024","2025"]
sales = [45,30,60,25,90]
plt.scatter(year,sales,color='blue',marker='x',label="All Cars")
plt.title("Sales Trend")
plt.ylabel("Sales(Cr)")
plt.xlabel("Year")
plt.legend()
plt.grid()
plt.savefig("sales.png")
plt.show()