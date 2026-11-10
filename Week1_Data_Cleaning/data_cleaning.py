
import pandas as pd

df = pd.read_excel("Cleaned_Dataset.xlsx")

print("FINAL DATA QUALITY REPORT")
print("-" * 30)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
print("\nTotal Missing Values:", df.isnull().sum().sum())

# Check duplicate OrderIDs
print("\nDuplicate OrderIDs:", df["OrderID"].duplicated().sum())

# Check invalid dates
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
print("Invalid Dates:", df["Date"].isnull().sum())

print("\nFinal Dataset Shape:", df.shape)
print("\nDATA TYPES:")
print(df.dtypes)

