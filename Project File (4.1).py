import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\ryan.murrells\PycharmProjects\pythonProject\vgsales.csv.csv", index_col= 0)

full_data = data.dropna()
sports_sales = full_data[full_data["Genre"]=="Sports"]
sports_sales_s = sports_sales.sort_values(["Year"], ascending= True)

sns.countplot(x="Year", data=sports_sales_s)
plt.ylabel("Quantity of Sports Sold")
plt.xticks(rotation=90)
plt.show()
