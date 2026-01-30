import pandas as pd

score = [45,60,75,90]

# series = pd.Series(score)
# print(series)
# print(series[0])

series = pd.Series(score,index=["Maths","Sciene","English","Social"])
print(series)
print(series["Maths"])