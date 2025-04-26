import os
import logging
from src.data import data_collection
from src.data import data_preprocessing
from src.features import feature_engineering
from src.models import train_model, predict_model

# Set up logging configuration
logging.basicConfig(filename='logs/automation_pipeline.log',  # You might need to create a 'logs' directory
                    level=logging.INFO,  # Capture all events with severity 'INFO' and above
                    format='%(asctime)s - %(levelname)s - %(message)s')  # Format for the log messages

def main():
    try:
        logging.info("Starting data collection...")
        data_collection.main()
        logging.info("Data collection completed successfully.")
        
        logging.info("Starting data preprocessing...")
        data_preprocessing.main()
        logging.info("Data preprocessing completed successfully.")
        
        logging.info("Starting feature engineering...")
        feature_engineering.main()
        logging.info("Feature engineering completed successfully.")
        
        logging.info("Starting model training...")
        train_model.main()
        logging.info("Model training completed successfully.")
        
        logging.info("Starting model prediction and evaluation...")
        predict_model.main()
        logging.info("Model prediction and evaluation completed successfully.")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
