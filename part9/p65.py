import matplotlib.pyplot as plt
year = ["2021","2022","2023","2024","2025"]
toyota = [45,30,60,25,90]
kia = [30,35,70,40,95]
plt.title("Sales Trend")
plt.ylabel("Sales(Cr)")
plt.xlabel("Year")
plt.legend()
plt.grid()
# plt.savefig("sales.png")
plt.stackplot(year,kia,toyota)
plt.show()