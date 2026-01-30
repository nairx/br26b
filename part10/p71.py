import pandas as pd
score = {
    "John" : [45,79,79],
    "Cathy":[90,34,34],
    "Mike":[35,23,23],
    "Amy":[70,30,30]
}

df = pd.DataFrame(score)
print(df)

df.drop_duplicates(inplace=True)
print(df)