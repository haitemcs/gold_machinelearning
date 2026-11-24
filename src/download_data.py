import os

import pandas as pd
import yfinance as yf


ticker = "GC=F"
start_date = "2000-01-01"
file_path = "data/gold_daily.csv"

os.makedirs("data", exist_ok=True)

gold = yf.download(
    ticker,
    start=start_date,
    interval="1d",
    auto_adjust=False,
    progress=False
)

if gold.empty:
    raise RuntimeError("No data was downloaded. Check your internet connection.")

# Handle the column format used by some yfinance versions.
if isinstance(gold.columns, pd.MultiIndex):
    gold.columns = gold.columns.get_level_values(0)

gold.columns = [str(column).lower().replace(" ", "_") for column in gold.columns]
gold.index.name = "date"
gold = gold[~gold.index.duplicated()].sort_index()

gold.to_csv(file_path)

print("Downloaded rows:", len(gold))
print("Date range:", gold.index.min().date(), "to", gold.index.max().date())
print("Saved to:", file_path)
