
import pandas as pd
import os

# ==================================
# STEP 1: LOAD DATASET
# ==================================

file_path = os.path.join("Dataset", "Dataset.xlsx")

df = pd.read_excel(file_path)

# ==================================
# STEP 2: DISPLAY DATASET
# ==================================

print("\n========== DATASET INFORMATION ==========")

print("\nFirst 5 Rows:")
print(df.head())

# ==================================
# STEP 3: DATASET SHAPE
# ==================================

print("\nDataset Shape:")
print(df.shape)

print("\nTotal Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

# ==================================
# STEP 4: COLUMN NAMES
# ==================================

print("\nColumn Names:")
print(df.columns.tolist())

# ==================================
# STEP 5: DATASET INFO
# ==================================

print("\nDataset Information:")
df.info()

# ==================================
# STEP 6: MISSING VALUES
# ==================================

print("\nMissing Values:")
print(df.isnull().sum())

# ==================================
# STEP 7: DUPLICATE VALUES
# ==================================

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# ==================================
# STEP 8: BASIC STATISTICS
# ==================================

print("\nBasic Statistics:")
print(df.describe())

# ==================================
# STEP 9: SUCCESS MESSAGE
# ==================================

print("\n=================================")
print("DATASET LOADED SUCCESSFULLY!")
print("=================================")

# ==================================
# STEP 10: PRODUCT-WISE SALES CHART
# ==================================

import matplotlib.pyplot as plt
import seaborn as sns

# Calculate Product-wise Sales
product_sales = df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False)

# Create Bar Chart
plt.figure(figsize=(10, 6))

sns.barplot(
    x=product_sales.index,
    y=product_sales.values
)

plt.title("Product-wise Total Sales", fontsize=16)
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

# Save Chart
plt.savefig("Charts/Product_Wise_Sales.png", dpi=300)

plt.show()

print("Product-wise Sales Chart Created Successfully!")

# ==================================
# STEP 11: MONTHLY SALES TREND
# ==================================

# Calculate Monthly Sales
monthly_sales = df.set_index("Date").resample("MS")["TotalPrice"].sum()

# Create Line Chart
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save Chart
plt.savefig("Charts/Monthly_Sales_Trend.png", dpi=300)

plt.show()

print("Monthly Sales Trend Chart Created Successfully!")

# ==================================
# STEP 12: PAYMENT METHOD PIE CHART
# ==================================

payment_counts = df["PaymentMethod"].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(
    payment_counts.values,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Payment Method Distribution", fontsize=16)

plt.tight_layout()

# Save Chart
plt.savefig("Charts/Payment_Method_Distribution.png", dpi=300)

plt.show()

print("Payment Method Pie Chart Created Successfully!")

# ==================================
# STEP 13: ORDER STATUS CHART
# ==================================

order_status = df["OrderStatus"].value_counts()

plt.figure(figsize=(9, 6))

sns.barplot(
    x=order_status.index,
    y=order_status.values
)

plt.title("Order Status Distribution", fontsize=16)
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")

plt.tight_layout()

plt.savefig("Charts/Order_Status_Distribution.png", dpi=300)

plt.show()

print("Order Status Chart Created Successfully!")
# ==================================
# STEP 15: QUANTITY VS TOTAL PRICE SCATTER PLOT
# ==================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Quantity",
    y="TotalPrice",
    hue="Quantity",
    s=70
)

plt.title("Quantity vs Total Price", fontsize=16)
plt.xlabel("Quantity")
plt.ylabel("Total Price")

plt.tight_layout()

# Save Chart
plt.savefig("Charts/Quantity_vs_TotalPrice.png", dpi=300)

plt.show()

print("Scatter Plot Created Successfully!")









