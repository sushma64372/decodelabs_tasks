import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_excel("Dataset for Data Analytics.xlsx")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Number of Rows and Columns
print("\nDataset Shape:")
print(df.shape)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())
print("Average Order Price:")
print(df["TotalPrice"].mean())
print("Median Order Price:")
print(df["TotalPrice"].median())
print("Total Orders:")
print(df["OrderID"].count())
print("Q1:")
print(df["TotalPrice"].quantile(0.25))
print("Q3:")
print(df["TotalPrice"].quantile(0.75))
Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

print("IQR:")
print(IQR)
lower_limit = Q1 - (1.5 * IQR)

print("Lower Limit:")
print(lower_limit)
upper_limit = Q3 + (1.5 * IQR)

print("Upper Limit:")
print(upper_limit)
outliers = df[
    (df["TotalPrice"] < lower_limit) |
    (df["TotalPrice"] > upper_limit)
]

print("Outliers:")
print(outliers[["OrderID", "TotalPrice"]])

print("Total Outliers:")
print(len(outliers))
plt.figure(figsize=(8, 5))

sns.boxplot(x=df["TotalPrice"])

plt.title("Boxplot of Total Price")
plt.xlabel("Total Price")

plt.show()
# Monthly Sales Analysis

df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["TotalPrice"].sum()

print("Monthly Sales:")
print(monthly_sales)
plt.figure(figsize=(12, 5))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.show()
df["Year"] = df["Date"].dt.year

yearly_sales = df.groupby("Year")["TotalPrice"].sum()

print("Yearly Sales:")
print(yearly_sales)
plt.figure(figsize=(8, 5))

yearly_sales.plot(kind="bar")

plt.title("Year-wise Sales Analysis")
plt.xlabel("Year")
plt.ylabel("Total Sales")

plt.show()
# Key Observations
print("\nKEY OBSERVATIONS")

print("1. Total 1200 orders are present in the dataset.")
print("2. Average order price is approximately Rs. 1053.97.")
print("3. There are 8 potential outliers in TotalPrice.")
print("4. Monthly sales fluctuate throughout the period.")
print("5. June 2024 recorded the highest monthly sales.")
print("6. CouponCode column contains 309 missing values.")
print("7. 2025 data is available only for January to June.")
