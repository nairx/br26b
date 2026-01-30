import pandas as pd
# score = {
#     "John" : [45,None,40,45,56,40,45,56,40],
#     "Cathy":[90,34,30,45,56,40,90,34,30],
#     "Mike":[35,23,45,56,40,90,56,40,90],
#     "Amy":[70,30,65,56,40,90,56,40,90]
# }

#2 D
# df = pd.DataFrame(score)
# print(df)

#2 D
# df = pd.DataFrame(score,index=["Maths","Science","English"])
# print(df)

#Read Columns
# print(df["John"])
# print(df[["John","Cathy"]])

#Read Rows
# print(df.loc["Maths"]) #label
# print(df.loc[0]) #label
# print(df.iloc[0])
# print(df.iloc[0:1])

#Modify 
# df["John"] = df["John"] + 10
# print(df)

#Add
# df["Total"] = df["John"] + df["Cathy"] + df["Mike"] + df["Amy"]
# print(df)

#filter
# print(df)
# print(df[df["John"]>40])
# print(df[(df["John"]>40) & (df["John"] < 50)])

# print(df)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe)

#Handling Missing Data
# print(df.isnull())
# print(df.dropna())
# df.fillna(100,inplace=True)
# print(df)


#sorting
# print(df.sort_values("Cathy"))
# print(df.sort_values("Cathy",ascending=False))



#group by
score = {
    "name" : ["John","John","John","Cathy","Cathy"],
    "marks":[90,34,30,45,56]
}
df = pd.DataFrame(score)
print(df)
print(df.groupby("name")["marks"].mean())







