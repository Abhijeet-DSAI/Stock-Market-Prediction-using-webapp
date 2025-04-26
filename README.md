# 📈 Stock Market Prediction WebApp

## Introduction
This project aims to predict stock prices for various companies listed in the Bombay Stock Exchange (BSE) using historical stock data.
This Streamlit app predicts and visualizes stock prices for major companies.
It features candlestick charts, prediction graphs, and feature importance analysis.
## Project Description
Stock markets are complex systems influenced by a myriad of factors, both internal and external. Predicting stock prices has always been a challenging task due to its high volatility and randomness. This project, however, attempts to decode some of this complexity by:

- **Collecting Historical Data**: Fetching comprehensive stock data from reliable sources like Yahoo Finance.
- **Advanced Preprocessing**: Cleaning and transforming the data to make it suitable for modeling.
- **Feature Engineering**: Extracting and creating new features that can provide more insights into the stock's behavior.
- **Modeling**: Using regression models to predict future stock prices based on historical data.
- **Web Interface**: Providing an interactive platform for users to select companies and view predictions.

---
## Table of Contents
- [Dataset](#dataset)
- [Preprocessing Steps](#preprocessing-steps)
- [Feature Engineering](#feature-engineering)
- [Model Training and Prediction](#model-training-and-prediction)
- [Web App](#web-app)
- [Usage](#usage)
- [Requirements](#requirements)

## Dataset
The dataset consists of historical stock data fetched from Yahoo Finance for various companies listed in the BSE.

## Preprocessing Steps
1. **Handling Missing Values**: Stocks might not be traded on certain days. We've filled these gaps using methods like forward fill.
2. **Outliers**: Identified and handled outliers.
3. **Data Transformation**: 
   - **Normalization/Standardization**: Standardized the closing prices.
   - **Log Transformation**: Applied to stabilize variances.
   - **Date Features Extraction**: Extracted day, month, quarter, and year.

## Feature Engineering
1. **Lagged Features**: Created lagged features for the past 5 days.
2. **Moving Averages**: Calculated moving averages for 30 and 60 days.
3. **RSI**: Calculated the Relative Strength Index.
4. **MACD**: Calculated the Moving Average Convergence Divergence.

## Model Training and Prediction
We've used a Linear Regression model for each company. The model is trained on historical data and can predict stock prices for a given date range.

- 
## 🛠️ Project Structure

```
Stock-Market-Prediction-Using-WebApp-main/
│
├── app.py                # Main web app (Streamlit)
├── main.py               # (Optional) Extra main script
│
├── src/
│   ├── data/
│   │   ├── data_collection.py
│   │   ├── data_preprocessing.py
│   │   └── feature_engineering.py
│   ├── models/
│   │   ├── train_model.py
│   │   └── predict_model.py
│   └── utils/
│       └── visualization.py
│
├── data/
│   ├── raw/              # Raw stock data
│   └── processed/        # Cleaned & processed data
│
├── models/               # Saved machine learning models
├── outputs/              # Saved graphs or prediction results
├── virtualenv/           # Virtual environment (optional)
└── README.md             # This file 📜
```

---

## 🔥 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Stock-Market-Prediction-WebApp.git
cd Stock-Market-Prediction-WebApp
```

### 2. Create Virtual Environment
```bash
python -m venv virtualenv
```

### 3. Activate Virtual Environment
- **Windows:**
  ```bash
  virtualenv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source virtualenv/bin/activate
  ```

### 4. Install Required Packages
```bash
pip install -r requirements.txt
```
*(Make sure you have a `requirements.txt` — you can generate it easily.)*

### 5. Run the Project Step-by-Step

| Step | Command | Purpose |
|:---|:---|:---|
| Collect data | `python src/data/data_collection.py` | Download raw stock data |
| Preprocess data | `python src/data/data_preprocessing.py` | Clean the raw data |
| Feature Engineering | `python src/data/feature_engineering.py` | Add new useful features |
| Train Model | `python src/models/train_model.py` | Train the prediction model |
| Predict Stock Prices | `python src/models/predict_model.py` | Generate future predictions |
| Visualize | `python src/utils/visualization.py` | Create graphs and plots |
| Launch Web App | `streamlit run app.py` | Open the app in your browser |


---

## 📸 Web app 
We've developed a Streamlit web app where users can:
- Select a company ticker.
- Choose a date range.
- View the predicted stock prices for the selected data range.

## Web app link
https://stock-market-prediction-using-webapp-fxokuwswrprazrufmczr34.streamlit.app/
  
**home page**

![image](https://github.com/user-attachments/assets/f9028486-74e4-4d27-aa38-2d8edfae21b0)

---
**🕯️ Candlestick chart tab**

![image](https://github.com/user-attachments/assets/dff9fd5a-0c4d-4c31-8045-a2c77bd72bc8)

---
**📈 Predicted Stock Prices Over Time tab**

![image](https://github.com/user-attachments/assets/6efe1fc9-887b-4c56-9e23-b7a869d9eccd)

---
**📊 Feature Importance**

![image](https://github.com/user-attachments/assets/c52950af-4a36-43fd-9c45-2ab23f4835f6)

---


# ✨ Special Thanks



