import os
import yfinance as yf
import pandas as pd

# List of stock symbols including GLD
symbols = ['AAPL', 'AMZN', 'TSLA', 'JNJ', 'JPM', 'SPY', 'EEM', 'GLD']

# Start and end dates
start_date1 = '2023-01-01'
end_date1 = '2023-12-31'
start_date2 = '2024-01-01'
end_date2 = '2024-04-01'


# Fetching historical data
def fetch_data(symbols, start_date1, end_date1, start_date2, end_date2):
    data = {}
    directory = '../data/raw'
    if not os.path.exists(directory):  # Check if directory exists
        os.makedirs(directory)
    for symbol in symbols:
        ticker = yf.Ticker(symbol)
        training = ticker.history(start=start_date1, end=end_date1)
        validation = ticker.history(start=start_date2, end=end_date2)
        training_path = os.path.join(directory, f'{symbol}_training_data.csv')
        validation_path = os.path.join(directory, f'{symbol}_validation_data.csv')
        training .to_csv(training_path)  # Save data to CSV
        validation.to_csv(validation_path)
        print(f'Data for {symbol} saved to {symbol}_data.csv')

fetch_data(symbols, start_date1, end_date1, start_date2, end_date2)
#%%
