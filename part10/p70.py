import pandas as pd
score = {
    "John" : [45,79,40,45,56,40,45,56,40],
    "Cathy":[90,34,30,45,56,40,90,34,30],
    "Mike":[35,23,45,56,40,90,56,40,90],
    "Amy":[70,30,65,56,40,90,56,40,90]
}
df = pd.DataFrame(score)
print(df)
# df.loc[0] = 100
# print(df)
# df.loc[0,"John"] = 100
# print(df)
for r in df.index:
    if df.loc[r,"John"] > 50:
        df.loc[r,"John"] = 100
print(df)
    