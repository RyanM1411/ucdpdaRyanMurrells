import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\ryan.murrells\PycharmProjects\pythonProject\vgsales.csv.csv", index_col= 0)

full_data = data.dropna()

sns.countplot(x="Genre", data=full_data)
plt.xticks(rotation=90)
plt.show()