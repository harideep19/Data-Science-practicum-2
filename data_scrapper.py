from binance.client import Client
import pandas as pd
import time

# Initialize client (no API key needed for public data)
client = Client()

symbol = "BTCUSDT"
interval = Client.KLINE_INTERVAL_1MINUTE

# Date range (60 days → ~80K+ rows)
start_str = "60 days ago UTC"

# Binance limit: max 1000 candles per request
limit = 1000

all_data = []

print("Downloading data...")

# Get initial data
klines = client.get_historical_klines(symbol, interval, start_str)

all_data.extend(klines)

print(f"Total rows fetched: {len(all_data)}")

# Convert to DataFrame
columns = [
    "Open time","Open","High","Low","Close","Volume",
    "Close time","Quote asset volume","Number of trades",
    "Taker buy base asset volume","Taker buy quote asset volume","Ignore"
]

df = pd.DataFrame(all_data, columns=columns)

# Convert timestamps
df['Open time'] = pd.to_datetime(df['Open time'], unit='ms')
df['Close time'] = pd.to_datetime(df['Close time'], unit='ms')

# Convert numeric columns
numeric_cols = ["Open","High","Low","Close","Volume"]
df[numeric_cols] = df[numeric_cols].astype(float)

# Keep useful columns only
df = df[["Open time","Open","High","Low","Close","Volume"]]

# Save to CSV
df.to_csv("btc_1min_60days.csv", index=False)

print("✅ Data saved as btc_1min_60days.csv")
print("Final shape:", df.shape)
print(df.head())