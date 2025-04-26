import yfinance as yf

def fetch_sensex_30_data(ticker_symbol, start_date, end_date):
    """
    Fetch historical stock data for a given ticker symbol from Yahoo Finance.
    
    Parameters:
    - ticker_symbol (str): The ticker symbol for the stock.
    - start_date (str): Start date in the format 'YYYY-MM-DD'.
    - end_date (str): End date in the format 'YYYY-MM-DD'.
    
    Returns:
    - DataFrame: A pandas DataFrame containing the historical stock data.
    """
    ticker_data = yf.Ticker(ticker_symbol)
    df = ticker_data.history(start=start_date, end=end_date)
    return df

# Test the function with a sample SENSEX 30 company, e.g., Reliance Industries Limited
ticker = "RELIANCE.BO"
start_date = "2018-01-01"
end_date = "2025-03-01"
data = fetch_sensex_30_data(ticker, start_date, end_date)
print(data.tail())

# If the data looks good, you can proceed to fetch data for other SENSEX 30 companies.
