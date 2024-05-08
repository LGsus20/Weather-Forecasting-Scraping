import pandas as pd
import LoadMyModel
import numpy as np
import math
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
from openpyxl import load_workbook

pd.set_option('display.max_columns', None)
PATH = r"https://raw.githubusercontent.com/LGsus20/Weather-Forecasting-Scraping/main/DATASETS/DATASET_Modified_Monthly_2021-2024.csv"
new_data = pd.read_csv(PATH)
MY_ERRORS_LIST_PATCHTST = []
MY_ERRORS_LIST_LSTM = []

# starting_row = 26280
starting_row = 26280
for i in range(len(new_data)-starting_row):
    i += 1
    ending_row = starting_row + 216 + i
    # DATA THE MODEL WILL GET TO PREDICT
    dataForPrediction = new_data.assign(unique_id=np.ones(len(new_data)))
    dataForPrediction = dataForPrediction.iloc[(starting_row+i):ending_row]
    dataForPrediction['ds'] = pd.to_datetime(dataForPrediction['ds'])
    # REAL DATA
    real_data = new_data.assign(unique_id=np.ones(len(new_data)))
    real_data = real_data.iloc[ending_row:(ending_row+1)]
    real_data['ds'] = pd.to_datetime(real_data['ds'])

    # CALL MODEL FOR PREDICTION
    Y_hat_df = LoadMyModel.LoadMyNeuralModel(dataForPrediction)
    Y_hat_df = Y_hat_df.iloc[[0]]

    # print("Forecast of the models:")
    # print(Y_hat_df.tail(1))
    # print("REAL VALUE:")
    # print(real_data["y"].iloc[0])
    # print("ERROR^2: ")
    MY_ERRORS_LIST_PATCHTST.append((float(Y_hat_df["PatchTST"].iloc[0]) - float(real_data["y"].iloc[0])) ** 2)
    MY_ERRORS_LIST_LSTM.append((float(Y_hat_df["LSTM"].iloc[0]) - float(real_data["y"].iloc[0])) ** 2)
    # print(MY_ERRORS_LIST_PATCHTST)

    print("RMSE PatchTST: ")
    myPatchTSTErr = math.sqrt(sum(MY_ERRORS_LIST_PATCHTST) / len(MY_ERRORS_LIST_PATCHTST))
    print(myPatchTSTErr)
    print("RMSE LSTM: ")
    myLSTMErr = math.sqrt(sum(MY_ERRORS_LIST_LSTM) / len(MY_ERRORS_LIST_LSTM))
    print(myLSTMErr)


myPatchTSTErr = math.sqrt(sum(MY_ERRORS_LIST_PATCHTST) / len(MY_ERRORS_LIST_PATCHTST))
myLSTMErr = math.sqrt(sum(MY_ERRORS_LIST_LSTM) / len(MY_ERRORS_LIST_LSTM))

print("My PatchTST RMSE: " + str(myPatchTSTErr))
print("My LSTM RMSE: " + str(myLSTMErr))
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