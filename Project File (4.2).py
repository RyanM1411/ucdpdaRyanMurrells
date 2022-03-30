import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\ryan.murrells\PycharmProjects\pythonProject\vgsales.csv.csv", index_col= 0)

full_data = data.dropna()
action_sales = full_data[full_data["Genre"]=="Action"]
action_sales_s = action_sales.sort_values(["Year"], ascending= True)

sns.countplot(x="Year", data=action_sales_s)
plt.xticks(rotation=90)
plt.ylabel("Quantity of Action Games Sold")
plt.show()