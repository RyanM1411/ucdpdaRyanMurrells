import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\ryan.murrells\PycharmProjects\pythonProject\vgsales.csv.csv", index_col= 0)
full_data = data.dropna()


top_platforms = full_data["Platform"]
print(top_platforms.value_counts().nlargest(5))

DS_sales = full_data[full_data["Platform"]=="DS"]
DS_Global = DS_sales["Global_Sales"]
np.DS_Global = np.array(DS_Global)

PS2_sales = full_data[full_data["Platform"]=="PS2"]
PS2_Global = PS2_sales["Global_Sales"]
np.PS2_Global = np.array(PS2_Global)

PS3_sales = full_data[full_data["Platform"]=="PS3"]
PS3_Global = PS3_sales["Global_Sales"]
np.PS3_Global = np.array(PS3_Global)

Wii_sales = full_data[full_data["Platform"]=="Wii"]
Wii_Global = Wii_sales["Global_Sales"]
np.Wii_Global = np.array(Wii_Global)

X360_sales = full_data[full_data["Platform"]=="X360"]
X360_Global = X360_sales["Global_Sales"]
np.X360_Global = np.array(X360_Global)

print("Top 5 DS Sales in Millions")
print(np.DS_Global[0:5])

print("Top 5 PS2 Sales in Millions")
print(np.PS2_Global[0:5])

print("Top 5 PS3 Sales in Millions")
print(np.PS3_Global[0:5])

print("Top 5 Wii Sales in Millions")
print(np.Wii_Global[0:5])

print("Top 5 X360 Sales in Millions")
print(np.X360_Global[0:5])

DS_avg = np.mean(np.DS_Global[0:100])
DS_avgerage = np.round(DS_avg, 2)
print("DS Average Sales for Top 100 games: " + str(DS_avgerage))

PS2_avg = np.mean(np.PS2_Global[0:100])
PS2_avgerage = np.round(PS2_avg, 2)
print("PS2 Average Sales for Top 100 games: " + str(PS2_avgerage))

PS3_avg = np.mean(np.PS3_Global[0:100])
PS3_avgerage = np.round(PS3_avg, 2)
print("PS3 Average Sales for Top 100 games: " + str(PS3_avgerage))

Wii_avg = np.mean(np.Wii_Global[0:100])
Wii_avgerage = np.round(Wii_avg, 2)
print("Wii Average Sales for Top 100 games: " + str(Wii_avgerage))

X360_avg = np.mean(np.X360_Global[0:100])
X360_avgerage = np.round(X360_avg, 2)
print("X360 Average Sales for Top 100 games: " + str(X360_avgerage))