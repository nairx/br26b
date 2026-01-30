import pandas as pd
score = {
    "Maths" : 45,
    "Science":90,
    "English":35,
    "Social":70
}

series = pd.Series(score)
print(series)

series = pd.Series(score,index=["Maths","Science"])
print(series)