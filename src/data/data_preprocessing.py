import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# === Function to preprocess a single DataFrame ===
def preprocess_data(df):
    # Ensure index is datetime
    df.index = pd.to_datetime(df.index)

    # Fill missing business days
    all_dates = pd.date_range(start=df.index.min(), end=df.index.max(), freq='B')
    df = df.reindex(all_dates)
    df.fillna(method='ffill', inplace=True)

    # Handle outliers in 'Close'
    rolling_mean = df['Close'].rolling(window=20).mean()
    rolling_std = df['Close'].rolling(window=20).std()
    upper_bound = rolling_mean + (2 * rolling_std)
    lower_bound = rolling_mean - (2 * rolling_std)
    df['Close'] = np.where((df['Close'] > upper_bound) | (df['Close'] < lower_bound), rolling_mean, df['Close'])

    # Standardization
    scaler = StandardScaler()
    df['Close_standardized'] = scaler.fit_transform(df[['Close']])

    # Log transformation
    df['Close_log'] = np.log1p(df['Close'])

    # Date features
    df['Day_of_Week'] = df.index.dayofweek
    df['Month'] = df.index.month
    df['Quarter'] = df.index.quarter
    df['Year'] = df.index.year

    # Normalize index
    df.index = df.index.normalize().tz_localize(None)

    return df


# === Main script ===
if __name__ == "__main__":
    input_directory = r"C:\Users\admin\OneDrive\Desktop\Stock-Market-Prediction-Using-WebApp-main\data\raw\SENSEX"
    output_directory = r"C:\Users\admin\OneDrive\Desktop\Stock-Market-Prediction-Using-WebApp-main\data\processed"

    # Make sure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        if filename.endswith(".csv"):
            try:
                print(f"Processing: {filename}")
                input_filepath = os.path.join(input_directory, filename)
                output_filepath = os.path.join(output_directory, f"processed_{filename}")

                # Load raw data
                data = pd.read_csv(input_filepath, parse_dates=['Date'], index_col='Date')

                # Preprocess
                processed_data = preprocess_data(data)

                # Save processed file
                processed_data.reset_index(inplace=True)
                processed_data.rename(columns={"index": "Date"}, inplace=True)
                processed_data.to_csv(output_filepath, index=False)

                print(f"Saved processed file to: {output_filepath}")

            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")
