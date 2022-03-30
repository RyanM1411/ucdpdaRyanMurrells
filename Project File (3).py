import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\ryan.murrells\PycharmProjects\pythonProject\vgsales.csv.csv", index_col= 0)

full_data = data.dropna()
data_by_year= full_data.sort_values(["Year"], ascending= True)

fig, ax =plt.subplots(1,3)
ax[0].plot(data_by_year["Year"], data_by_year["JP_Sales"])
ax[1].plot(data_by_year["Year"], data_by_year["NA_Sales"])
ax[2].plot(data_by_year["Year"], data_by_year["EU_Sales"])
ax[0].set_xlabel("Japanese Sales 1980-2020")
ax[1].set_xlabel("North American Sales 1980-2020")
ax[2].set_xlabel("European Sales 1980-2020")
ax[0].set_ylabel("Sales in Millions")
plt.show()

