import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\ryan.murrells\PycharmProjects\pythonProject\vgsales.csv.csv", index_col= 0)

full_data = data.dropna()

from bokeh.plotting import figure
from bokeh.io import output_file, show

data_by_year = full_data.sort_values(["Year"], ascending= True)

fig = figure(x_axis_label="Years", y_axis_label="Sales in Millions")
fig.circle(x=data_by_year["Year"], y=data_by_year["JP_Sales"], color="red")
fig.circle(x=data_by_year["Year"], y=data_by_year["NA_Sales"], color="blue")
fig.circle(x=data_by_year["Year"], y=data_by_year["EU_Sales"], color="green")
fig.circle(x=data_by_year["Year"], y=data_by_year["Other_Sales"], color="yellow")

output_file("Sales_Comparison_Over_the_Years.html")
show(fig)

