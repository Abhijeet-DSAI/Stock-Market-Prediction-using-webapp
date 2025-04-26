import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import os

# --- FUNCTIONS ---
def load_model(ticker):
    model_path = f'src/models/saved_model/processed_{ticker}_model.pkl'
    model = joblib.load(model_path)
    return model

def make_prediction(model, date_range):
    predictions = np.random.rand(len(date_range))  # Dummy predictions (replace with model.predict if available)
    return predictions

def load_actual_data(ticker):
    csv_path = f'data/processed/processed_{ticker}.BO.csv'
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        return df
    else:
        st.error(f"Actual data file not found for {ticker}")
        return None

# --- STREAMLIT APP STARTS ---
st.set_page_config(page_title="Stock Market Prediction App", layout="wide")

# --- CREATOR BADGE ---
st.markdown(
    """
    <div style="text-align: right; font-size: 18px; margin-bottom: -30px;">
        Made by 🚀 <a href="https://www.linkedin.com/in/abhijeet-prakash-04aa65237/" target="_blank" style="text-decoration: none; color: #4CAF50;">Abhijeet</a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.title('📈 Stock Market Prediction App')

# Sidebar for settings
with st.sidebar:
    st.header("Settings")

    # Theme Switcher
    theme = st.selectbox("🌓 Choose Theme", ("Light Mode", "Dark Mode"))

    if theme == "Dark Mode":
        plotly_template = "plotly_dark"
        plt.style.use('dark_background')
    else:
        plotly_template = "plotly_white"
        plt.style.use('default')

    tickers = [
        "ASIANPAINT", "AXISBANK", "BAJAJ-AUTO", "BAJFINANCE",
        "BAJAJFINSV", "BHARTIARTL", "DRREDDY", "HCLTECH",
        "HDFC", "HDFCBANK", "HEROMOTOCO", "HINDUNILVR",
        "ICICIBANK", "INDUSINDBK", "INFY", "ITC",
        "KOTAKBANK", "LT", "M&M", "MARUTI", "NESTLEIND",
        "NTPC", "ONGC", "POWERGRID", "RELIANCE", "SBIN",
        "SUNPHARMA", "TATAMOTORS", "TATASTEEL", "TCS", "TECHM"
    ]
    selected_ticker = st.selectbox('Select a Ticker:', tickers)
    start_date = st.date_input('Start Date')
    end_date = st.date_input('End Date')

    predict_button = st.button('🚀 Run Prediction')

# --- MAIN CONTENT ---
if predict_button:
    model = load_model(selected_ticker)
    date_range = pd.date_range(start=start_date, end=end_date)
    predictions = make_prediction(model, date_range)
    actual_data = load_actual_data(selected_ticker)

    if actual_data is not None:
        actual_data['Date'] = pd.to_datetime(actual_data['Date'])

    st.success("✅ Prediction completed!")

    tab1, tab2, tab3 = st.tabs(["🕯️ Candlestick Chart", "📈 Predictions", "📊 Feature Importance"])

    with tab1:
        st.subheader("🕯️ Candlestick Chart")
        if actual_data is not None and all(col in actual_data.columns for col in ['Open', 'High', 'Low', 'Close']):
            fig = go.Figure(data=[go.Candlestick(
                x=actual_data['Date'],
                open=actual_data['Open'],
                high=actual_data['High'],
                low=actual_data['Low'],
                close=actual_data['Close']
            )])

            fig.update_layout(
                title=f'{selected_ticker} Candlestick Chart',
                xaxis_title='Date',
                yaxis_title='Price',
                xaxis_rangeslider_visible=False,
                template=plotly_template,
                height=600
            )
            st.plotly_chart(fig)
        else:
            st.warning("Candlestick data (Open, High, Low, Close) not available.")

    with tab2:
        st.subheader("📈 Predicted Stock Prices Over Time")
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(date_range, predictions, label='Predicted Prices', color='blue')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        ax.set_title(f'Predicted Prices for {selected_ticker}')
        ax.legend()
        st.pyplot(fig)

    with tab3:
        st.subheader("📊 Feature Importance")
        if hasattr(model, 'feature_importances_'):
            features = ['Open', 'High', 'Low', 'Close', 'Volume']
            importances = model.feature_importances_

            fig, ax = plt.subplots(figsize=(8, 5))
            ax.barh(features, importances[:len(features)], color='skyblue')
            ax.set_xlabel('Importance')
            ax.set_title('Feature Importance')
            st.pyplot(fig)
        else:
            st.info("Feature importance not available for this model.")
