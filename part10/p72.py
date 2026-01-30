import pandas as pd
score = {
    "John" : [45,79,79],
    "Cathy":[90,34,34],
    "Mike":[35,23,23],
    "Amy":[70,30,30]
}

df = pd.DataFrame(score)
df.to_csv("./part10/score.csv")
df.to_excel("./part10/score.xlsx",index=False)