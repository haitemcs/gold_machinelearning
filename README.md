# Gold Machine Learning

This project uses daily gold futures data from Yahoo Finance:

- **Ticker:** `GC=F` (COMEX Gold Futures)
- **Interval:** 1 day
- **Start date:** 2000-01-01

## Notebooks

### Gold Direction Prediction.ipynb

This is the main notebook. It predicts whether the next trading day's closing price will go **UP** or **DOWN**.

It compares:
- Logistic Regression
- Random Forest
- PyTorch Neural Network

It reports accuracy, balanced accuracy, precision, recall, F1-score and ROC-AUC.

### Volatility Forecasting.ipynb

This is a separate experiment. It predicts the next day's normalized high-low range. It does **not** predict whether gold will go up or down.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/download_data.py
jupyter notebook
```

Open the notebook you want to run and execute its cells from top to bottom.

The downloaded CSV is saved locally at `data/gold_daily.csv` and is not committed to GitHub.

## Important

The direction model uses historical prices and technical features. It is a learning and research project, not a reliable trading signal. Check its performance on unseen dates and compare it with simple baselines before drawing conclusions.
