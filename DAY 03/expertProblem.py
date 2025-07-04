# Problem: Identify Top Performing Students from Exam Data
# You are given a dataset of students with their scores in Maths, Physics, Chemistry, and Biology. Your task is to:
# Calculate each student's average score.
# Label students as:
# "Topper" if average ≥ 90
# "Average" if 60 ≤ average < 90
# "Weak" if average < 60
import pandas as pd
scorefile = pd.read_csv("C:/Users/Faraaz/OneDrive/Documents/LEARNING/30-Days-AIML-Challenge/DAY 03/student_scores.csv")
scorefile["Average"]= scorefile[["Maths","Physics","Chemistry","Biology"]].mean(axis=1)
print(scorefile["Average"])

scorefile["Label"] = pd.cut(x=scorefile["Average"],bins =[0,60,90,101],labels=["Weak","Average","Topper"],right=False)

print(scorefile["Label"])