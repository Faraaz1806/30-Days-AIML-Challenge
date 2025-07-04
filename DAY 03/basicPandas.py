import pandas as pd
firstList = pd.Series([1,2,3,4,5], index = ["a","b","c","d","e"])
print(firstList)
dataFrame = pd.DataFrame({"Names":["Faraaz","Rehan","Aziz"],"Ages":[20,10,8]})
print(dataFrame)