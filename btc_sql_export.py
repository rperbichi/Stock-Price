import sqlite3
import pandas as pd
import kagglehub

# Dowloading data
path = kagglehub.dataset_download("mczielinski/bitcoin-historical-data")
print("Path to dataset files:", path)

