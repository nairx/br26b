import matplotlib.pyplot as plt
year = ["2021","2022","2023","2024","2025"]
toyota = [45,30,60,25,90]
kia = [30,35,70,40,95]
plt.plot(year,toyota,color='blue',marker='o',linestyle="dashed",label="Toyota Cars")
plt.plot(year,kia,color='green',marker='o',linestyle="dashed",label="Kia Cars")
plt.title("Sales Trend")
plt.ylabel("Sales(Cr)")
plt.xlabel("Year")
plt.legend()
plt.grid()
# plt.savefig("sales.png")
plt.show()