import pandas as pd
import numpy as np
data = pd.read_csv(r"C:\Users\ryan.murrells\PycharmProjects\pythonProject\vgsales.csv.csv", index_col= 0)

null = pd.isnull(data)
test = data.iloc[175:185, 2:4]
total_missing = pd.isnull(data).sum().sum()


full_data = data.dropna()


x = 0
for lab, row  in data.iterrows():
    x+=1
    if x> 10:
        break
    print(str(lab) + ": " + row ["Name"])

