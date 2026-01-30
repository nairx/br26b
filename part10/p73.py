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