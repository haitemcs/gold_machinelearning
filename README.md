# Gold Machine Learning

Daily gold futures volatility forecasting using Yahoo Finance historical data.

This project adapts the workflow from the BTC **Volatility Forecasting** notebook:
- PyTorch neural network
- XGBoost regressor
- Ridge regression baseline
- Chronological train/test split
- Daily OHLCV feature engineering

## Data

The project uses Yahoo Finance ticker **GC=F** (COMEX Gold Futures), interval **1d**. Run the notebook or `src/download_data.py` to download historical data and save it to `data/gold_daily.csv`.

The CSV is generated locally and is not committed to the repository. Yahoo Finance data availability and history can change.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

Open `Volatility Forecasting.ipynb` and run the cells from top to bottom.

## Target

The first version forecasts the **next trading day's normalized high-low range**:

`next_day_range / rolling_20_day_average_range`

This is a volatility proxy, not a directional buy/sell signal or a guaranteed price forecast.

## Important

- Features are built only from information available at the prediction time.
- The split is chronological; scalers are fitted on training data only.
- The test set is held out from model fitting.
- Evaluate against simple baselines before interpreting model performance.
- This project is for educational research, not financial advice.
