import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Directory paths
data_directory = r"C:\Users\admin\OneDrive\Desktop\Stock-Market-Prediction-Using-WebApp-main\data\processed"
models_directory = r"C:\Users\admin\OneDrive\Desktop\Stock-Market-Prediction-Using-WebApp-main\src\models\saved_model"

# Ensure models directory exists
if not os.path.exists(models_directory):
    os.makedirs(models_directory)

# List all processed data files
files = [f for f in os.listdir(data_directory) if f.endswith('.csv')]
print("Files found for training:", files)

for file in files:
    try:
        print(f"\nProcessing file: {file}")
        data_path = os.path.join(data_directory, file)
        data = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')
        
        if 'Close' not in data.columns:
            print(f"Skipped {file} — 'Close' column not found.")
            continue

        # Split data
        X = data.drop('Close', axis=1)
        y = data['Close']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        
        # Train model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Save model
        ticker_symbol = file.split('.')[0]
        model_path = os.path.join(models_directory, f"{ticker_symbol}_model.pkl")
        joblib.dump(model, model_path)
        print(f"Model saved: {model_path}")

    except Exception as e:
        print(f"Error processing {file}: {e}")

print("\nAll models trained and saved!")
