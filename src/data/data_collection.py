import yfinance as yf
import pandas as pd
import os

def fetch_sensex_30_data(ticker_symbol, start_date, end_date, save_path):
    """
    Fetch historical stock data for a given ticker symbol from Yahoo Finance and save it.
    
    Parameters:
    - ticker_symbol (str): The ticker symbol for the stock.
    - start_date (str): Start date in the format 'YYYY-MM-DD'.
    - end_date (str): End date in the format 'YYYY-MM-DD'.
    - save_path (str): Directory where the fetched data should be saved.
    
    Returns:
    - None
    """
    ticker_data = yf.Ticker(ticker_symbol)
    df = ticker_data.history(start=start_date, end=end_date)
    df.to_csv(os.path.join(save_path, f"{ticker_symbol}.csv"))

sensex_30_tickers = [
    "ASIANPAINT.BO", "AXISBANK.BO", "BAJAJ-AUTO.BO", "BAJFINANCE.BO", 
    "BAJAJFINSV.BO", "BHARTIARTL.BO", "DRREDDY.BO", "HCLTECH.BO", 
    "HDFC.BO", "HDFCBANK.BO", "HEROMOTOCO.BO", "HINDUNILVR.BO", 
    "ICICIBANK.BO", "INDUSINDBK.BO", "INFY.BO", "ITC.BO", 
    "KOTAKBANK.BO", "LT.BO", "M&M.BO", "MARUTI.BO", "NESTLEIND.BO", 
    "NTPC.BO", "ONGC.BO", "POWERGRID.BO", "RELIANCE.BO", "SBIN.BO", 
    "SUNPHARMA.BO", "TATAMOTORS.BO", "TATASTEEL.BO", "TCS.BO", "TECHM.BO"
]

if __name__ == "__main__":
    start_date = "2018-01-01"
    end_date = "2025-03-01"
    save_directory = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw', 'SENSEX')

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    for ticker in sensex_30_tickers:
        print(f"Fetching data for {ticker}...")
        fetch_sensex_30_data(ticker, start_date, end_date, save_directory)
