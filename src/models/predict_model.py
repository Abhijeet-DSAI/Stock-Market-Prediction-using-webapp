import os
import pandas as pd
import joblib
import pickle

# Directory paths
data_directory = r"C:\Users\admin\OneDrive\Desktop\Stock-Market-Prediction-Using-WebApp-main\data\processed"
models_directory = r"C:\Users\admin\OneDrive\Desktop\Stock-Market-Prediction-Using-WebApp-main\src\models\saved_model"
results_directory = r'C:\Users\admin\OneDrive\Desktop\Stock-Market-Prediction-Using-WebApp-main\src\models\predict_result'  # Directory to save the results

# Ensure results directory exists
if not os.path.exists(results_directory):
    os.makedirs(results_directory)

# List all processed data files
files = [f for f in os.listdir(data_directory) if f.endswith('.csv')]

for file in files:
    # Load data
    data_path = os.path.join(data_directory, file)
    data = pd.read_csv(data_path, parse_dates=['Date'], index_col='Date')
    
    # Split data (assuming you've already split the data during training and have a function for it)
    X = data.drop('Close', axis=1)
    y = data['Close']
    # Assuming last 20% is test data (adjust as per your actual split)
    split_index = int(0.8 * len(data))
    X_test = X.iloc[split_index:]
    y_test = y.iloc[split_index:]
    
    # Load model
    ticker_symbol = file.split('.')[0]  # Assuming file name is the ticker symbol
    model_path = os.path.join(models_directory, f"{ticker_symbol}_model.pkl")
    model = joblib.load(model_path)
    
    # Predict
    predictions = model.predict(X_test)
    
    # Save actual and predicted values for visualization
    results = pd.DataFrame({
        'Actual': y_test,
        'Predicted': predictions
    })
    results_path = os.path.join(results_directory, f"{ticker_symbol}_results.csv")
    results.to_csv(results_path)

print("Predictions made and saved for all companies!")
