import pandas as pd

# Load all CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine all data
df = pd.concat([df1, df2, df3])

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# 🔥 FIX: clean price column
df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

# Ensure quantity is numeric
df["quantity"] = df["quantity"].astype(int)

# Create sales
df["sales"] = df["quantity"] * df["price"]

# Keep only needed columns
df = df[["sales", "date", "region"]]

# Save
df.to_csv("output.csv", index=False)

print("✅ Fixed and done!")