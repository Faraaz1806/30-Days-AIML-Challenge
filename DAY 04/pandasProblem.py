import pandas as pd
data = {"Names":["Faraaz","Rehan","Huzaifa"],
        "Maths":[60,90,50],
        "Physics": [55,98,62],
        "Chemistry":[45,98,100]}
df = pd.DataFrame(data)
# print(df)

df["Total Marks"] = df["Maths"]+df["Physics"]+df["Chemistry"]
# print(df)

# print(df[df["Total Marks"]>240])

print(df[df["Chemistry"]==df["Chemistry"].max()])

print(df["Chemistry"].mean())