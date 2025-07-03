# Problem 2: Clean the Data
# Tumhare paas ye list hai:
# data = [25, None, 0, 47, None, 82, 0, 13]
# Task:
# List me se None aur 0 hatao
# Nayi list cleaned_data me daalo
# print(cleaned_data)
 
data = [25, None, 0, 47, None, 82, 0, 13]
cleaned_list = []
for element in data:
    if element != None and element != 0:
        cleaned_list.append(element)
print("The cleaned Version of the list is \n",cleaned_list)