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


def fetch_options_data(symbols, start_date, end_date):
    directory = '../data/raw'
    if not os.path.exists(directory):
        os.makedirs(directory)  # Ensure the directory exists

    for symbol in symbols:
        ticker = yf.Ticker(symbol)  # Corrected to use 'symbol' instead of 'symbols'
        hist_data = ticker.history(start=start_date, end=end_date)

        # Assuming hist_data contains options dates - this part seems off; you likely need another step to access options data.
        # hist_data.options would not typically work unless defined elsewhere in your code or context.
        # This would be the correct method if hist_data were replaced by something like ticker.options
        if ticker.options:
            options_dates = ticker.options  # Gets expiration dates
            option_chain = ticker.option_chain(options_dates[0])  # Get options data for the first available expiration
            combined_options = pd.concat([option_chain.calls, option_chain.puts])

            # Saving the data to CSV files
            option_chain.calls.to_csv(f'{directory}/{symbol}_calls.csv')
            option_chain.puts.to_csv(f'{directory}/{symbol}_puts.csv')
            print(f'Option Data for {symbol} saved to {directory}')
        else:
            print(f"No options data available for {symbol}")

# Example call to the function
options_symbols = ['^NDX', '^GSPC', '^VIX', '^RUT']
fetch_options_data(options_symbols, start_date2, end_date2)
#%%
