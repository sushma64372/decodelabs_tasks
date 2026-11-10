import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("sales.db")

# Read CSV file
df = pd.read_csv("dataset.csv")

# Import data into SQL table
df.to_sql("orders", conn, if_exists="replace", index=False)

print("Dataset imported successfully!")

# Check total records
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM orders")

print("Total Records:", cursor.fetchone()[0])

conn.close()