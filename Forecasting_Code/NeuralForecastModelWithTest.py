import torch
from datetime import datetime
from neuralforecast import NeuralForecast
from neuralforecast.models import LSTM, PatchTST
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

print("Starting run, current time:", datetime.now().time())

PATH = r"https://raw.githubusercontent.com/LGsus20/Weather-Forecasting-Scraping/main/DATASETS/DATASET_Modified_Monthly_2021-2023.csv"
Y_df = pd.read_csv(PATH).assign(unique_id=np.ones(len(pd.read_csv(PATH))))
Y_df['ds'] = pd.to_datetime(Y_df['ds'])
print("DATA:\n")
print(Y_df)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("Device:", device)

models = [
    PatchTST(input_size=216, h=6, max_steps=2000).to(device),
    LSTM(input_size=216, h=6, max_steps=2000).to(device)
]

nf = NeuralForecast(
    models=models,
    freq='h',
)

# Split data into training and testing sets
train_df = Y_df.iloc[:-250]  # Use all but the last 100 rows for training
test_df = Y_df.iloc[-6:]   # Use the last 100 rows for testing

# Train the model
nf.fit(df=train_df)
predictions = nf.predict(df=test_df)
print("Predictions:")
print(predictions)

# Extract actual values
actual_values = test_df['y'].values

predictions_PTST = predictions["PatchTST"]
predictions_LSTM = predictions["LSTM"]

# Calculate MAE
maePTST = mean_absolute_error(actual_values, predictions_PTST)
maeLSTM = mean_absolute_error(actual_values, predictions_LSTM)

print("Mean Absolute Error (MAE):", maePTST)
print("Mean Absolute Error (MAE):", maeLSTM)

# Calculate RMSE
rmsePTST = mean_squared_error(actual_values, predictions_PTST, squared=False)
rmseLSTM = mean_squared_error(actual_values, predictions_LSTM, squared=False)
print("Root Mean Squared Error (RMSE):", rmsePTST)
print("Root Mean Squared Error (RMSE):", rmseLSTM)

nf.save("WindForecasting")

print("Finished, current time:", datetime.now().time())
