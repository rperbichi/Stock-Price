import sqlite3
import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("andrewmvd/sp-500-stocks")
# print("Path to dataset files:", path) 

csv_file = "sp500_companies.csv"
df = pd.read_csv(csv_file)

# Deleting exchange column
df.drop(columns=["Exchange"], inplace=True)

# Handling errors
df["Marketcap"] = pd.to_numeric(df["Marketcap"], errors="coerce")
df["Ebitda"] = pd.to_numeric(df["Ebitda"], errors="coerce")
df["Revenuegrowth"] = pd.to_numeric(df["Revenuegrowth"], errors="coerce")

conn = sqlite3.connect("sp500_companies.db")
df.to_sql("companies", conn, if_exists="replace", index=False)

# Export cleaned data as CSV for Power BI
df.to_csv("sp500_companies_cleaned.csv", index=False)

conn.close()
