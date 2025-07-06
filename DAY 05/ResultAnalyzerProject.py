# Project Name: Student Report Generator
# Problem Statement:
# Schools and teachers need an easy way to check students' marks, calculate totals, decide pass or fail, and find the toppers.

# Goal:
# 1) Build a Python program that:
# 2) Reads student marks of three subject Physics, Chemistry and Maths from a CSV or Excel file
# 3) Calculates total and average
# 4) Checks if each student has passed or failed
# 5) Finds the topper(s)

# Shows the final report:

import pandas as pd
file_path = input("Enter the file in which marks of three subject that is Physics, Chemistry, Maths path ending with .csv or .xlsx: \n")
if(file_path.endswith(".csv")):
    df = pd.read_csv(file_path)
elif(file_path.endswith(".xlsx")):
    df = pd.read_excel(file_path)
else:
    print("Invalid file_path , File path must end with .csv or .xlsx")
print("Original Data\n",df)
df["Total Marks"] = df["Physics"]+df["Chemistry"]+df["Maths"]

df["Average Marks"] = (df["Total Marks"])/3
df["Pass/Fail"]=df["Average Marks"].apply(lambda x: "Pass" if x>=70 else "Fail")
df = df.sort_values(by = "Average Marks", ascending=False)
df["Rank"] = range(1,len(df)+1)
print("Final Report: \n",df)
