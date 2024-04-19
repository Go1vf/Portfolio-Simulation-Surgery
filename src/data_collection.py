import os
import yfinance as yf
import pandas as pd

# List of stock symbols including GLD
symbols = ['AAPL', 'AMZN', 'TSLA', 'JNJ', 'JPM', 'SPY', 'EEM', 'GLD']

# Start and end dates
start_date = '2023-04-01'
end_date = '2024-04-01'


# Fetching historical data
def fetch_data(symbols, start_date, end_date):
    data = {}
    directory = '../data/raw'
    if not os.path.exists(directory):  # Check if directory exists
        os.makedirs(directory)
    for symbol in symbols:
        ticker = yf.Ticker(symbol)
        data = ticker.history(start=start_date, end=end_date)
        file_path = os.path.join(directory, f'{symbol}_one_year_data.csv')
        data.to_csv(file_path)  # Save data to CSV
        print(f'Data for {symbol} saved to {symbol}_one_year_data.csv')


fetch_data(symbols, start_date, end_date)
#%%
