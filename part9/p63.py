import matplotlib.pyplot as plt
sales = [45,30,60,25,10]
cars = ["Maruti","Tata","Ford","Kia","Toyota"]

plt.pie(sales,labels=cars,autopct="%1.2f%%")
plt.title("Sales 2025")

plt.show()