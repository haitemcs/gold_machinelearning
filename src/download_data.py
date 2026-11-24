from pathlib import Path

import pandas as pd
import yfinance as yf


TICKER = "GC=F"
START_DATE = "2000-01-01"
OUTPUT_PATH = Path("data/gold_daily.csv")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    data = yf.download(
        TICKER,
        start=START_DATE,
        interval="1d",
        auto_adjust=False,
        progress=False,
    )

    if data.empty:
        raise RuntimeError(
            "Yahoo Finance returned no data. Check your internet connection "
            "and confirm that the ticker is available."
        )

    # Recent yfinance versions can return MultiIndex columns for one ticker.
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data.columns = [str(column).lower().replace(" ", "_") for column in data.columns]
    data.index.name = "date"
    data = data[~data.index.duplicated(keep="first")].sort_index()
    data.to_csv(OUTPUT_PATH)

    print(f"Downloaded {len(data):,} daily rows for {TICKER}.")
    print(f"Date range: {data.index.min().date()} to {data.index.max().date()}")
    print(f"Saved CSV: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
