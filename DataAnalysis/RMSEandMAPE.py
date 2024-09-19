import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

# Load data from CSV
file_path = r"C:\Users\Jesus\Downloads\forecasting\Weather-Forecasting-Scraping\Forecasting_Code\recordedValues.csv"
data = pd.read_csv(file_path)

# Convert 'ds' column to datetime
data['ds'] = pd.to_datetime(data['ds'])

# Calculate RMSE
rmseTst = np.sqrt(mean_squared_error(data['RealVal'], data['PatchTST']))
print("RMSE PatchTST:", rmseTst)

rmseLSTM = np.sqrt(mean_squared_error(data['RealVal'], data['LSTM']))
print("RMSE LSTM:", rmseLSTM)

# Calculate MAE
maeTst = mean_absolute_error(data['RealVal'], data['PatchTST'])
print("MAE PatchTST:", maeTst)

maeLSTM = mean_absolute_error(data['RealVal'], data['LSTM'])
print("MAE LSTM:", maeLSTM)

# Calculate MAPE
def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

mapeTst = mean_absolute_percentage_error(data['RealVal'], data['PatchTST'])
print("MAPE PatchTST:", mapeTst)

mapeLSTM = mean_absolute_percentage_error(data['RealVal'], data['LSTM'])
print("MAPE LSTM:", mapeLSTM)

# # Plotting
# plt.figure(figsize=(10, 6))
#
# plt.plot(data['ds'], data['RealVal'], label='RealVal', marker=',')
# plt.plot(data['ds'], data['PatchTST'], label='PatchTST', marker='.', color='green')
# plt.plot(data['ds'], data['LSTM'], label='LSTM', marker='.')
#
# plt.xlabel('Datetime')
# plt.ylabel('Values')
# plt.title('Comparison of real values and PatchTST')
# plt.legend()
#
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
