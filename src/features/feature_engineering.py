import pandas as pd
import os
import numpy as np

def add_lagged_features(df, column_name, lag_count=5):
    for i in range(1, lag_count + 1):
        df[f"{column_name}_Lagged_{i}"] = df[column_name].shift(i)
    return df

def add_technical_indicators(df):
    # Simple Moving Averages
    df['SMA_30'] = df['Close'].rolling(window=30).mean()
    df['SMA_60'] = df['Close'].rolling(window=60).mean()
    
    # RSI
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # MACD
    short_ema = df['Close'].ewm(span=12, adjust=False).mean()
    long_ema = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = short_ema - long_ema
    df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()
    
    return df

def clean_data(df):
    # Drop the "Unnamed: 0" column if it exists
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    # Drop rows with missing values
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    directory = r"C:\Users\admin\OneDrive\Desktop\Stock-Market-Prediction-Using-WebApp-main\data\processed"
    
    for filename in os.listdir(directory):
        if filename.startswith("processed_") and filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            
            data = pd.read_csv(filepath, parse_dates=['Date'])
            
            # Add lagged features
            data = add_lagged_features(data, 'Close', lag_count=5)
            
            # Add technical indicators
            data = add_technical_indicators(data)
            
            # Clean the data
            data = clean_data(data)
            
            # Update the existing CSV with the processed data
            data.to_csv(filepath, index=False)
