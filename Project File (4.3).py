import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\ryan.murrells\PycharmProjects\pythonProject\vgsales.csv.csv", index_col= 0)

full_data = data.dropna()
rp_sales = full_data[full_data["Genre"]=="Role-Playing"]
rp_sales_s = rp_sales.sort_values(["Year"], ascending= True)

sns.countplot(x="Year", data=rp_sales_s)
plt.xticks(rotation=90)
plt.ylabel("Quantity of Role Playing Games Sold")
plt.show()