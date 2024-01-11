# Stock Market Forecasting with LSTM

## Overview
This project involves the analysis and visualization of stock market data using various Python libraries. The goal is to extract meaningful insights from minute-by-minute stock data and present them through visualizations.

## Libraries Used
- NumPy: For numerical operations.
- Pandas: For data manipulation and analysis.
- Matplotlib: For creating static, interactive, and animated visualizations.
- Seaborn: For making statistical graphics.
- mplfinance: For financial market data visualization.
- Scikit-learn: For data preprocessing and scaling.

## Data Importing
The data is imported from Google Drive using the `drive.mount` method provided by Google Colab.

## Data Preprocessing
Includes converting date-time columns to DateTime format and filtering stock market data for trading hours.

## Visualization
Several types of visualizations are created:
- Minute-by-Minute Closing Price Series
- Day-by-Day Closing Price Series
- Candlestick Chart with Volume

## Normalization Techniques
Two normalization techniques are applied to the data:
- MinMaxScaler: Scales the data within a specified range, typically between 0 and 1.
- Z-Scaler (StandardScaler): Transforms the data to have a mean of 0 and a standard deviation of 1.

## LSTM Model
A custom LSTM (Long Short-Term Memory) neural network model is created using PyTorch for predicting stock prices.

## Resampling
Data is resampled to decrease the frequency to make the PyTorch module flexible for the DataLoader.

## Model Training and Evaluation
The LSTM model is trained and evaluated on the stock price data, and the performance is measured using the Mean Squared Error loss function.