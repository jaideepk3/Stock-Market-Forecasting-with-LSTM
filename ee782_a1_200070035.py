# -*- coding: utf-8 -*-
"""EE782_A1_200070035.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XfEnG1MMqeeg0Mk-OK48mHdNvSQptjHj

[Explanation Video](https://drive.google.com/file/d/1gDDcEnN_iYZRyjTMuEXRueSu5e8l_xgu/view?usp=sharing)

### Importing required libraries
"""

import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler,StandardScaler
!pip install mplfinance
import mplfinance as mpf

#connecting to the google drive
from google.colab import drive
drive.mount('/content/drive')

"""### Importing data from the Google drive"""

data = pd.read_csv("/content/drive/MyDrive/EE782_data/A_1min.csv")
data

print(data.columns) #columns in a dataset

# import matplotlib.dates as mdates

"""## Minute-by-Minute Closing Price Series for all data"""

# data['Date Time'] = pd.to_datetime(data['Date Time'], format='%Y-%m-%d %H:%M:%S')

# # Create a plot of the minute-by-minute closing price series
# plt.figure(figsize=(12, 6))
# plt.plot(data['Date Time'], data['Close'], label='Closing Price', linewidth=1)
# plt.title('Minute-by-Minute Closing Price Series')
# plt.xlabel('Time')
# plt.ylabel('Closing Price')
# plt.grid(True)
# plt.legend()
# plt.show()

"""## Minute-by-Minute Closing Price Series for the years 2007-2008"""

# # Define the time range you want to filter
# start_date = '2007-01-01'
# end_date = '2008-12-31'

# # Filter the data based on the specified date range
# filtered_data = data[(data['Date Time'] >= start_date) & (data['Date Time'] <= end_date)]

# # Create a plot of the minute-by-minute closing price series for the filtered data
# plt.figure(figsize=(12, 6))
# plt.plot(filtered_data['Date Time'], filtered_data['Close'], label='Closing Price', linewidth=1)
# plt.title('Minute-by-Minute Closing Price Series (2007-2008)')
# plt.xlabel('Time')
# plt.ylabel('Closing Price')
# plt.grid(True)
# plt.legend()
# plt.show()

"""## Function to plot Minute-by-Minute Closing Price for any year or a duration

"""

# def plot_minute_by_minute_closing_prices(data, start_year, end_year):
#   # Define the start and end dates based on the input years
#   start_date = f'{start_year}-01-01'
#   end_date = f'{end_year}-12-31'
#   # Filter the data based on the specified date range
#   filtered_data = data[(data['Date Time'] >= start_date) & (data['Date Time'] <= end_date)]
#   # Create a plot of the minute-by-minute closing price series for the filtered data
#   fig, ax = plt.subplots(figsize=(12, 6))
#   ax.plot(filtered_data['Date Time'], filtered_data['Close'], label='Closing Price', linewidth=1)

#   # Format the x-axis to show abbreviated month names
#   ax.xaxis.set_major_locator(mdates.MonthLocator())
#   ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

#   plt.title(f'Minute-by-Minute Closing Price Series ({start_year}-{end_year})')
#   plt.xlabel('Time')
#   plt.ylabel('Closing Price')
#   plt.grid(True)
#   plt.legend()
#   plt.show()

# # Call the function with the desired start and end years
# plot_minute_by_minute_closing_prices(data, start_year=2009, end_year=2009)

# def plot_day_by_day_closing_prices(data, start_year, end_year):
#   # Define the start and end dates based on the input years
#   start_date = f'{start_year}-01-01'
#   end_date = f'{end_year}-12-31'
#   # Filter the data based on the specified date range
#   filtered_data = data[(data['Date Time'] >= start_date) & (data['Date Time'] <= end_date)]
#   # Create a daily resampled DataFrame for closing prices
#   daily_data = filtered_data.resample('D', on='Date Time').last()  # Resample to daily frequency
#   # Create a plot of the day-by-day closing price series for the filtered data
#   fig, ax = plt.subplots(figsize=(12, 6))
#   ax.plot(daily_data.index, daily_data['Close'], label='Closing Price', linewidth=1)

#   # Format the x-axis to show months and years
#   ax.xaxis.set_major_locator(mdates.MonthLocator())
#   ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
#   x_ticks = daily_data.index[11::21]
#   ax.set_xticks(x_ticks)


#   plt.title(f'Day-by-Day Closing Price Series ({start_year}-{end_year})')
#   plt.xlabel('Time')
#   plt.ylabel('Closing Price')
#   plt.xticks(rotation=45)
#   plt.grid(True)
#   plt.legend()
#   plt.show()

# # Call the function with the desired start and end years
# plot_day_by_day_closing_prices(data, start_year=2007, end_year=2007)

"""I got wrong plot because I forgot to consider the stock market closing time which led to missing data points

## Function to plot Day-by-Day Closing Price for any year or a duration
"""

# def plot_day_by_day_closing_prices(data, start_year, end_year):
#   # Filter the data for the specified date range and closing time
#   filtered_data = data[(data['Date Time'].dt.year >= start_year) & (data['Date Time'].dt.year <= end_year) & (data['Date Time'].dt.time == pd.to_datetime('15:59:00').time())]  # Assuming close time is 15:59:00

#   # Extract time and closing price data
#   time = filtered_data['Date Time']
#   closing_price = filtered_data['Close']

#   plt.figure(figsize=(12, 6))
#   plt.plot(time, closing_price)
#   plt.title(f'Closing Prices vs. Time for {start_year} to {end_year}')
#   plt.xlabel('Time')
#   plt.ylabel('Close Price')

#   # Set x-axis ticks to display a new month approximately every 21 days
#   x_ticks = time.iloc[11::21]  # Assuming that every 21st data point corresponds to a new month
#   plt.xticks(x_ticks, x_ticks.dt.strftime('%b'))

#   plt.show()

# # Call the function with the desired start and end years
# plot_day_by_day_closing_prices(data, start_year=2007, end_year=2007)

"""### Filtering Stock Market Data for Trading Hours"""

# Converting Date Time Column to DateTime Format
data['Date Time'] = pd.to_datetime(data['Date Time'], format='%Y-%m-%d %H:%M:%S')

# Define the start and close times for the stock market
start_time = pd.to_datetime('09:30:00').time()   # Starting time of the stock market
close_time = pd.to_datetime('15:59:00').time()  # A minute before the closing time
end_time = pd.to_datetime('16:00:00').time()     # Closing time

# Filter the stock market data for the specified trading hours
crt_data = data[(data['Date Time'].dt.time >= start_time) & (data['Date Time'].dt.time <= end_time)]
crt_data

"""### Visualization of Minute-by-Minute Closing Price Series"""

# Title: Visualization of Minute-by-Minute Closing Price Series

# Extract the relevant columns from crt_data
time = crt_data['Date Time']  # Extract the timestamp data
closing_price = crt_data['Close']  # Extract the closing price data

# Create a plot of the minute-by-minute closing price series
plt.figure(figsize=(12, 6))  # Create a new figure with specified size
plt.plot(time, closing_price, label='Closing Price', linewidth=1)  # Plot the closing price over time
plt.title('Minute-by-Minute Closing Price Series')  # Set the plot title
plt.xlabel('Time')  # Label the x-axis as 'Time'
plt.ylabel('Closing Price')  # Label the y-axis as 'Closing Price'
plt.grid(True)  # Add a grid to the plot
plt.legend()  # Display the legend
plt.show()  # Show the plot

"""### Visualizing Minute-by-Minute Closing Price Series for a Specified Date Range"""

# Define start_date and end_date for the date range of interest
start_date = '2021-01-01'
end_date = '2021-12-31'

# Filter the 'crt_data' DataFrame based on the specified date range
filtered_data = crt_data[(crt_data['Date Time'] >= start_date) & (crt_data['Date Time'] <= end_date)]

# Extract the relevant columns from the filtered data
time = filtered_data['Date Time']         # Extract the timestamp
closing_price = filtered_data['Close']    # Extract the closing price

# Create a plot of the minute-by-minute closing price series
plt.figure(figsize=(12, 6))
plt.plot(time, closing_price, label='Closing Price', linewidth=1)
plt.title(f'Minute-by-Minute Closing Price Series\n({start_date} to {end_date})')  # Set the plot title
plt.xlabel('Time')                         # Label for the x-axis
plt.ylabel('Closing Price')                # Label for the y-axis
plt.grid(True)                             # Display gridlines
plt.legend()                               # Display legend
plt.show()                                 # Show the plot

"""### Plot Minute-by-Minute Closing Prices for a Specified Year Range"""

# Function to plot minute-by-minute closing prices for a specified year range
def plot_minute_by_minute_closing_prices(start_year, end_year, data):
    # Define start_date and end_date based on the input years
    start_date = f'{start_year}-01-01'
    end_date = f'{end_year}-12-31'
    # Filter data based on the specified date range
    filtered_data = data[(data['Date Time'] >= start_date) & (data['Date Time'] <= end_date)]
    # Extract the relevant columns from filtered_data
    time = filtered_data['Date Time']
    closing_price = filtered_data['Close']
    # Create a plot of the minute-by-minute closing price series
    plt.figure(figsize=(12, 6))
    plt.plot(time, closing_price, label='Closing Price', linewidth=1)
    plt.title(f'Minute-by-Minute Closing Price Series\n({start_year} to {end_year})')
    plt.xlabel('Time')
    plt.ylabel('Closing Price')
    plt.grid(True)
    plt.legend()
    plt.show()

# Call the function with the desired start_year, end_year, and data
plot_minute_by_minute_closing_prices(start_year=2021, end_year=2021, data=crt_data)

"""### Plot Day-by-Day Closing Prices for a Specified Year Range"""

def plot_day_by_day_closing_prices(start_year, end_year, data):
  # Define start_date and end_date based on the input years
  start_date = f'{start_year}-01-01'
  end_date = f'{end_year}-12-31'
  # Filter data based on the specified date range and closing time
  filtered_data = data[(data['Date Time'] >= start_date) & (data['Date Time'] <= end_date) & (data['Date Time'].dt.time == pd.to_datetime('15:59:00').time())]
  # Extract time and closing price data
  time = filtered_data['Date Time']
  closing_price = filtered_data['Close']
  # Create a plot of day-by-day closing price series
  plt.figure(figsize=(12, 6))
  plt.plot(time, closing_price)
  plt.title(f'Closing Prices vs. Time for {start_year} to {end_year}')
  plt.xlabel('Time')
  plt.ylabel('Close Price')
  # Set x-axis ticks to display a new month approximately every 21 days
  x_ticks = time.iloc[11::21]  # Assuming that every 21st data point corresponds to a new month
  plt.xticks(x_ticks, x_ticks.dt.strftime('%b'))
  plt.grid(True)
  plt.show()

# Call the function with the desired start_year, end_year, and data
plot_day_by_day_closing_prices(start_year=2021, end_year=2021, data=crt_data)

crt_data.set_index('Date Time', inplace=True)
# Set the 'Date Time' column as the index for the DataFrame 'crt_data'.
# This operation replaces the default integer index with the 'Date Time' values,
# making it easier to access and work with time-series data.

"""### Candlestick Chart with Volume for a Specific Time Range"""

# Define the start and end times for the plot as datetime objects
start = pd.to_datetime('2018-01-03 09:30:00')
end = pd.to_datetime('2018-01-03 10:30:00')

# Extract data for the specified time range
subset_data = crt_data[(crt_data.index >= start) & (crt_data.index <= end)]

# Create a subplot for volume on the secondary y-axis
volume = mpf.make_addplot(subset_data["Volume"], panel=1, color="blue", width=0.7, ylabel="Volume", secondary_y=True)

# Create the candlestick chart with volume on the secondary y-axis
mpf.plot(subset_data, type='candle', addplot=[volume], style='binance', title="Stocks on 3rd Jan, 2018 (with Volume)", ylabel="Price ($)")

"""### Observations:
**Volume Fluctuations**: We observe that at the beginning and end of the trading day, there is a significant surge in the trading volume, indicating a higher level of shares being bought and sold during those periods.

### Normalization Techniques:

* **MinMaxScaler**: One normalization technique applied to the data involves scaling it using the Min-Max scaling method. This method transforms the data so that it falls within a specified range, typically between 0 and 1, preserving the relationships between values while ensuring they are all within a consistent scale.

* **Z-Scaler**: Another normalization method is the z-scaler, which transforms the data to have a mean (average) of 0 and a standard deviation of 1. This technique is useful for standardizing data and making it easier to compare and analyze, particularly when dealing with features or variables that have different units or scales.

### Min-Max Scaling for Data Normalization
"""

# Function to perform Min-Max scaling on the given dataset
def minmax_scaling(data):
    min_max_scaler = MinMaxScaler()  # Create a MinMaxScaler object for data normalization
    data_scaled = min_max_scaler.fit_transform(data)  # Normalize the data, excluding the datetime index
    data_minmax = pd.DataFrame(data_scaled, columns=data.columns)  # Convert the normalized data to a DataFrame
    data_minmax.insert(0, 'Date Time', data.index.values)  # Insert the DateTime column at the beginning for easy reference
    return data_minmax

# Call the minmax_scaling function on 'crt_data'
normalized_data = minmax_scaling(crt_data)

# applying the min-max scaling and plotting the normalized values
plot_minute_by_minute_closing_prices(2020,2020,minmax_scaling(crt_data))

"""### Z-Scale the Data with Date Time Column Insertion"""

# Define a function for Z-scaling the data
def zscaling(data):
    z_score_scaler = StandardScaler()   # Create a Z-score scaler object
    data_scaled = z_score_scaler.fit_transform(data)    # Use the Z-score scaler to normalize the data
    data_zscore = pd.DataFrame(data_scaled, columns=data.columns)   # Create a DataFrame with column names from the original data
    data_zscore.insert(0, 'Date Time', data.index.values)   # Insert the 'Date Time' column at the beginning for easier plotting
    return data_zscore    # Return the Z-scaled data with the inserted 'Date Time' column

# Call the zscaling function with the input data (crt_data)
zscaling(crt_data)

# applying the z-scaling and plotting the normalized values
plot_minute_by_minute_closing_prices(2020,2020,zscaling(crt_data))

"""### Observations:
* Min-Max scaling is preferred over the z-score normalization because it ensures that the normalized values always range between 0 and 1.
* In contrast, the z-score normalization can result in values below zero, which may pose challenges when calculating profits or losses based on percentages, as negative values could lead to calculation issues.

## Creating a Custom LSTM Model with Specified Input Dimensions, Units, and Layers
"""

import torch
import torch.nn as nn

"""LSTM Neural Network Module"""

# Define a custom LSTM module using PyTorch's nn.Module
class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers):
        super(LSTM, self).__init__()

        # Define the LSTM layer with input size, hidden size, and number of layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)

        # Define the fully connected (linear) layer connecting LSTM hidden to output
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # Forward pass through the LSTM
        out, _ = self.lstm(x)

        # Extract the output of the last time step
        out = self.fc(out[:, -1, :])
        return out

"""Resampling the data to decrease the frequency to make the pytorch module flexible for the dataloader"""

def resample_data(data, frequency='1d'):
    """
    Resample the data to a lower frequency.

    Parameters:
    - data: The input data to be resampled.
    - frequency: The desired frequency for resampling (e.g., '1d' for daily, '1H' for hourly).

    Returns:
    - Resampled data with aggregated values.
    """
    aggregation_rules = {
        "Open": "first",
        "High": "max",
        "Low": "min",
        "Close": "last",
        "Volume": "sum"
    }

    # Perform resampling with the specified frequency
    resampled_data = data.resample('{}'.format(frequency), origin='start').agg(aggregation_rules).dropna()
    return resampled_data

"""We need to set up data loaders for training and testing the LSTM model. In this process, we define the sequence length as the input size for the model, and the following upcoming value serves as the model's output. This arrangement allows us to train and evaluate the model effectively."""

from torch.utils.data import Dataset, DataLoader

class StockDataset(Dataset):
    """
    Custom dataset for stock market data.

    Parameters:
    - data: The stock market data.
    - sequence_length: The length of input sequences.
    """

    def __init__(self, data, sequence_length):
        self.data = data
        self.sequence_length = sequence_length

    def __len__(self):
        return len(self.data) - self.sequence_length

    def __getitem__(self, idx):
        idx += self.sequence_length
        features = self.data.iloc[idx - self.sequence_length:idx, :]
        target = self.data.iloc[idx, 3]  # Assuming 'close' is the target
        return torch.tensor(features.values, dtype=torch.float32), torch.tensor(target, dtype=torch.float32)

resampled_data = resample_data(crt_data, frequency='1d')

import time  # Import the time module

"""### Model Training, and Evaluation for LSTM-based Stock Price Prediction"""

# Step 1: Prepare the data for normalization
# Select the relevant columns (Open, High, Low, Close, Volume) from the dataset
data_for_normalization = resampled_data[['Open', 'High', 'Low', 'Close', 'Volume']]

# Step 2: Apply Min-Max scaling to normalize the data
# Create a Min-Max scaler object
minmax_scaler = MinMaxScaler()

# Normalize the selected data using the scaler
normalized_data = minmax_scaler.fit_transform(data_for_normalization)

# Step 3: Create a DataFrame with the normalized data
# Convert the normalized data array into a DataFrame
normalized_df = pd.DataFrame(normalized_data, columns=data_for_normalization.columns, index=data_for_normalization.index)

# Step 4: Define the training and testing data periods
# Select the training data from the normalized DataFrame (from 2005 to 2020)
train_data = normalized_df['2005':'2020']

# Select the testing data from the normalized DataFrame (from 2021 to 2022)
test_data = normalized_df['2021':'2022']

# Step 5: Define the sequence length for input data
# Adjust the sequence length as needed for your specific use case
sequence_length = 10

# Step 6: Create datasets and data loaders for training and testing
# Create a dataset for training using the training data and sequence length
train_dataset = StockDataset(train_data, sequence_length)

# Create a dataset for testing using the testing data and sequence length
test_dataset = StockDataset(test_data, sequence_length)

# Create data loaders for training and testing with batch size and optional shuffling
batch_size = 64
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# Step 7: Define the LSTM model architecture
# Define the number of input features, hidden units, output size, and number of layers
input_size = 5  # Number of input features: Close, High, Low, Open, Volume
hidden_size = 64
output_size = 1  # Assuming 'close' is the target variable
num_layers = 2

# Create an instance of the LSTM model
model = LSTM(input_size, hidden_size, output_size, num_layers)

# Step 8: Define the loss function (Mean Squared Error) and optimizer (Adam)
# Define the loss function for regression tasks (Mean Squared Error)
criterion = nn.MSELoss()

# Define the optimizer (Adam optimizer) and specify the learning rate
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Step 9: Training loop
# Define the number of training epochs (adjust as needed)
num_epochs = 25  # Increase to 25 epochs

# Record the start time of training
start_time = time.time()

for epoch in range(num_epochs):
    # Set the model in training mode
    model.train()

    # Initialize the total loss for this epoch for training
    train_total_loss = 0

    # Iterate over batches of training data
    for batch_features, batch_targets in train_loader:
        # Zero the gradients
        optimizer.zero_grad()

        # Forward pass: Compute model predictions
        outputs = model(batch_features)

        # Calculate the loss between predicted and target values for training
        train_loss = criterion(outputs, batch_targets.unsqueeze(1))

        # Backpropagation: Compute gradients and update model parameters
        train_loss.backward()
        optimizer.step()

        # Accumulate the loss for this batch for training
        train_total_loss += train_loss.item()

    # Calculate and print the average training loss for this epoch
    avg_train_loss = train_total_loss / len(train_loader)
    print(f'Epoch [{epoch + 1}/{num_epochs}], Training Loss: {avg_train_loss}')

# Record the end time of training
end_time = time.time()

# Calculate and print the total training time
training_time = end_time - start_time
print(f'Total training time: {training_time:.2f} seconds')

# Step 10: Evaluation loop
# Now, perform the evaluation loop for 25 epochs separately

# Record the start time of evaluation
start_time = time.time()

model.eval()  # Set the model in evaluation mode

for epoch in range(num_epochs):
    # Initialize the total loss for testing
    test_total_loss = 0

    # Iterate over batches of testing data
    for batch_features, batch_targets in test_loader:
        # Forward pass: Compute model predictions
        outputs = model(batch_features)

        # Calculate the loss between predicted and target values for testing
        test_loss = criterion(outputs, batch_targets.unsqueeze(1))

        # Accumulate the loss for this batch for testing
        test_total_loss += test_loss.item()

    # Calculate and print the average testing loss for this epoch
    avg_test_loss = test_total_loss / len(test_loader)
    print(f'Epoch [{epoch + 1}/{num_epochs}], Testing Loss: {avg_test_loss}')

# Record the end time of evaluation
end_time = time.time()

# Calculate and print the total evaluation time
evaluation_time = end_time - start_time
print(f'Total evaluation time: {evaluation_time:.2f} seconds')

"""### Further Evaluation of Model on Test Data"""

# Set the model in evaluation mode
model.eval()

# Initialize the test loss
test_loss = 0

# Use torch.no_grad() to disable gradient calculation during testing
with torch.no_grad():
    # Iterate over batches of test data
    for batch_features, batch_targets in test_loader:
        # Perform a forward pass to obtain model predictions
        outputs = model(batch_features)

        # Calculate the loss between predicted and target values
        loss = criterion(outputs, batch_targets.unsqueeze(1))

        # Accumulate the loss for this batch
        test_loss += loss.item()

# Calculate the average test loss
avg_test_loss = test_loss / len(test_loader)

# Print the average test loss
print(f'Test Loss: {avg_test_loss}')

"""### Predict Stock Prices Using Trained LSTM Model"""

# Set the model to evaluation mode
model.eval()

# Initialize lists to store predicted and actual values using list comprehensions
predicted_values = [model(batch_features).squeeze(1).tolist() for batch_features, _ in test_loader]
actual_values = [batch_targets.tolist() for _, batch_targets in test_loader]

# Convert the lists to numpy arrays for easier manipulation
y_p = np.concatenate(predicted_values)  # Concatenate predicted values into a numpy array
a_v = np.concatenate(actual_values)      # Concatenate actual values into a numpy array

# Return the predicted values
y_p

"""### Stock Trading Module for Simulation"""

def trading_module(initial_balance, predicted_values, actual_values):
    # Initialize stock quantity and balance
    stock_quantity = 0
    balance = initial_balance

    # Iterate through the time steps
    for i in range(1, len(predicted_values)):
        # Check if predicted price is higher than the previous time step
        if predicted_values[i] > predicted_values[i-1]:
            # Calculate the number of stocks to buy with available balance
            no_of_stocks_to_buy = balance // actual_values[i-1]
            # Increase stock quantity
            stock_quantity += no_of_stocks_to_buy
            # Decrease balance after buying stocks
            balance -= no_of_stocks_to_buy * actual_values[i-1]
        # Check if predicted price is lower than the previous time step
        elif predicted_values[i] < predicted_values[i-1]:
            # Sell all stocks and add the resulting balance
            balance += stock_quantity * actual_values[i-1]
            # Reset stock quantity to zero
            stock_quantity = 0

    # If there are remaining stocks at the end, sell them
    balance += stock_quantity * actual_values[-1]
    # Reset stock quantity to zero
    stock_quantity = 0

    # Return the final balance
    return balance

"""### Stock Trading Simulation"""

# Initialize the initial balance (starting amount of cash)
initial_balance = 1000000

# Replace 'y_p' with the predicted price values
predicted_values = y_p

# Replace 'a_v' with the actual price values
actual_values = a_v

# Use the 'trading_module' function to simulate trading based on predictions and actual values
final_balance = trading_module(initial_balance, predicted_values, actual_values)

# Print the final balance after trading
print(f"Final Balance: {final_balance}")

"""### Comparison of Predicted and Actual Stock Prices"""

# Import the necessary library for plotting
import matplotlib.pyplot as plt

# Create a new figure with a specific size
plt.figure(figsize=(12, 6))

# Plot the actual values in blue
plt.plot(actual_values, label='Actual', color='blue')

# Plot the predicted values in red
plt.plot(predicted_values, label='Predicted', color='red')

# Add a legend to distinguish between actual and predicted values
plt.legend()

# Add a title to the plot
plt.title('Comparison of Predicted and Actual Stock Prices')

# Label the x and y axes for clarity
plt.xlabel('Time')
plt.ylabel('Price')

# Display the plot
plt.show()

"""8a. The provided data indicates that the prediction error (MSE) remains stable during testing, suggesting that the model's performance does not significantly worsen as you move further from the last training period. the training loss significantly decreases, indicating the model's ability to fit the training data. Testing implies there is good generalization

8b. The provided data and analysis focus on the prediction error (MSE) of a model and do not directly address the profitability of trading with bid-ask spreads and commissions taken into account.

8c. The obtained LSTM model results show stable prediction error, but assessing profitability compared to a buy-and-hold strategy requires a more comprehensive analysis, including actual returns, transaction costs, and market conditions.

9a. To modify the model to use multiple stock prices as inputs to predict a single stock, you would need to adjust the input size and potentially the data preprocessing. However, the provided code primarily focuses on the prediction of a single stock's closing price using its historical data. To include multiple stock prices as inputs, you should:

1. **Data Preprocessing**: Expand the dataset to include the historical data of the additional stocks you want to use as input features alongside the target stock.

2. **Input Size**: Adjust the `input_size` to match the number of input features, which will now include the historical prices of multiple stocks.

3. **Model Architecture**: Modify the LSTM model architecture to handle the increased input dimensions, considering the historical prices of multiple stocks.

4. **Training and Testing Data**: Ensure that the dataset is correctly structured with the data of all selected stocks for both training and testing.

5. **Evaluation**: Assess whether including multiple stock prices improves predictions by comparing the model's performance (e.g., MSE) against a baseline model that uses only the historical data of the single target stock.

This modification aims to capture potential relationships between the target stock and other stocks to improve prediction accuracy. However, the effectiveness of this approach may vary based on the specific stocks chosen and their relationships.

## References:
* most of the references are from ChatGPT and Bard which helped me find modules and helped in how to implement few functions
* LSTM model references
  * https://www.datacamp.com/tutorial/lstm-python-stock-market
  * https://www.kaggle.com/code/faressayah/stock-market-analysis-prediction-using-lstm
  * https://www.analyticsvidhya.com/blog/2021/12/stock-price-prediction-using-lstm/

* Finding out balance and comparison of Predicted and Actual Stock Prices, I discussed with Deepika(20D110013)
"""