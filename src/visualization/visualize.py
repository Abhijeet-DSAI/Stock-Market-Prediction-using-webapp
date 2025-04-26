import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_predictions(actual, predicted, ticker_symbol):
    """
    Plot actual vs predicted values.
    
    Parameters:
    - actual: Actual values (ground truth)
    - predicted: Predicted values from the model
    - ticker_symbol: Name of the company or ticker symbol for title
    """
    
    plt.figure(figsize=(14, 7))
    plt.plot(actual.index, actual.values, label='Actual', color='blue')
    plt.plot(actual.index, predicted, label='Predicted', color='red', linestyle='--')
    
    plt.title(f"Actual vs Predicted for {ticker_symbol}")
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Save the figure if needed
    # plt.savefig(f"visualizations/{ticker_symbol}_predictions.png")
    
    plt.show()

# Directory paths
results_directory = r"C:\Users\admin\OneDrive\Desktop\Stock-Market-Prediction-Using-WebApp-main\src\models\predict_result"

# List all results files
files = [f for f in os.listdir(results_directory) if f.endswith('_results.csv')]

for file in files:
    # Load results
    data_path = os.path.join(results_directory, file)
    data = pd.read_csv(data_path, parse_dates=True, index_col=0)
    
    # Extract actual and predicted values
    actual = data['Actual']
    predicted = data['Predicted']
    
    # Plot
    ticker_symbol = file.split('_')[0]  # Extracting ticker symbol from filename
    plot_predictions(actual, predicted, ticker_symbol)
