import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Basic info
print("\n--- Dataset Info ---")
print(df.info())

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Last 5 Rows ---")
print(df.tail())

print("\n--- Statistical Summary ---")
print(df.describe())

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Set date as index
df.set_index("date", inplace=True)

print("\nDate column converted and set as index")

df.to_csv("data_cleaned.csv")
print("\n✅ Cleaned dataset saved as data_cleaned.csv")