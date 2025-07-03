# Problem:
# You’re given a list of ages of different people.
# You need to classify them as:
# Teen = 13 to 17
# Adult = 18 to 59
# Senior = 60+
# Ignore: None, < 13, and negative values
# Ignore any value that is None or negative (invalid)

# Input:
# ages = [16, 25, None, 70, -3, 45, 13, 61, 18, 59, None, 8, 60]
# Task:
# Write a Python program that:
# Loops through the ages list
# Skips invalid values (None or negative)
# Creates a new list of labels like:
# ['Teen', 'Adult', 'Senior', 'Adult', 'Teen', 'Senior', 'Adult', 'Adult', 'Teen', 'Senior']
# Maintain the order — just skip invalid entries.
ages = [16, 25, None, 70, -3, 45, 13, 61, 18, 59, None, 8, 60]
cleaned_list = []
for element in ages:
    if element != None and element > 0:
        cleaned_list.append(element)
print("The cleaned Version of the list is \n",cleaned_list)
finalList = []
t = "Teen"
a = "Adult"
s = "Senior"
for ages in cleaned_list:
    if ages > 13 and ages < 18:
        finalList.append(t)
    elif ages >= 18 and ages <= 60:
        finalList.append(a)
    elif ages > 60:
        finalList.append(s)
print(finalList)