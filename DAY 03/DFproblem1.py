# Problem 1: Student Marks Table
# Create a DataFrame from this data:
# Name: ["Ayaan", "Faraaz", "Zahid", "Omar"]
# Math: [78, 92, 85, 69]
# Science: [88, 90, 81, 73]
import pandas as pd
df = pd.DataFrame({"Names":["Ayaan", "Faraaz", "Zahid", "Omar"],
                   "Maths":[78, 92, 85, 69],
                   "Science":[88, 90, 81, 73]})
# print(df)
# print(df.head(2))
# print(df[["Names","Maths"]])
# print(df[df["Science"]>80]["Names"])
print(df[df["Names"]=="Faraaz"]["Science"])