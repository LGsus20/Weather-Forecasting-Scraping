import pandas as pd
import LoadMyModel
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from openpyxl import load_workbook

pd.set_option('display.max_columns', None)
PATH = r"C:\Users\Jesus\Downloads\forecasting\Weather-Forecasting-Scraping\DATASETS\DATASET_Modified_Monthly_2021-2024.csv"


# starting_row = 26280
starting_row = 26281
ending_row = starting_row + 6
new_data = pd.read_csv(PATH)

# DATA THE MODEL WILL GET TO PREDICT
dataForPrediction = new_data.assign(unique_id=np.ones(len(new_data)))
dataForPrediction = dataForPrediction.iloc[starting_row:ending_row]
dataForPrediction['ds'] = pd.to_datetime(dataForPrediction['ds'])
# REAL DATA
real_data = new_data.assign(unique_id=np.ones(len(new_data)))
real_data = real_data.iloc[ending_row:(ending_row+6)]
real_data['ds'] = pd.to_datetime(real_data['ds'])

# CALL MODEL FOR PREDICTION
Y_hat_df = LoadMyModel.LoadMyNeuralModel(dataForPrediction)


# Show prediction and actual values
print("Forecast of the models:")
print(Y_hat_df.tail(6))


# Does a RMSE test
def rmse(predicted_values):
    return mean_squared_error(real_data["y"], predicted_values, squared=False)

def mae(predicted_values):
    return mean_absolute_error(real_data["y"], predicted_values)

# Predicted values:
y_LSTM = Y_hat_df['LSTM']
y_PatchTST = Y_hat_df['PatchTST']

# Add real values
Y_hat_df = pd.merge(Y_hat_df, real_data)


# Name of the Excel file
excel_file = f'Benchmark_{starting_row}.xlsx'
Y_hat_df.to_excel(f'Benchmark_{starting_row}.xlsx', index=False)
wb = load_workbook(excel_file)
ws = wb.active

ws.append([''])
ws.append(['RMSE LSTM:', rmse(y_LSTM)])
ws.append(['RMSE PatchTST:', rmse(y_PatchTST)])
ws.append(['MAE LSTM:', mae(y_LSTM)])
ws.append(['MAE PatchTST:', mae(y_PatchTST)])
wb.save(excel_file)