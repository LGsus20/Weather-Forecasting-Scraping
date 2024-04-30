import LoadMyModel
import numpy as np
import pandas as pd
import LoadMyModel
from openpyxl import load_workbook

pd.set_option('display.max_columns', None)

# Call LoadMyModel.py for predictions
Y_hat_df = LoadMyModel.LoadMyModel()

# ENTER THE ACTUAL VALUES:
y_true = [3.6, 3.6, 1.8, 0.4, 2.9, 4.7]
Y_hat_df = Y_hat_df.assign(RealValues=y_true)

# Show prediction and actual values
print("Forecast of the models:")
print(Y_hat_df)


# Does a RMSE test
def rmse(y_pred):
    y_true = np.array(Y_hat_df['RealValues'])
    y_pred = np.array(y_pred)
    return np.sqrt(np.mean((y_true - y_pred) ** 2))

# Predicted values:
y_AutoArima = Y_hat_df['AutoARIMA']
y_AutoRegressive = Y_hat_df['AutoRegressive']
y_AutoTheta = Y_hat_df['AutoTheta']

print()
print("RMSE AutoARIMA:", rmse(y_AutoArima))
print("RMSE AutoRegressive:", rmse(y_AutoRegressive))
print("RMSE AutoTheta:", rmse(y_AutoTheta))


# Name of the Excel file
excel_file = 'Y_hat_df.xlsx'
Y_hat_df.to_excel('Y_hat_df.xlsx', index=False)
wb = load_workbook(excel_file)
ws = wb.active

# Add your text at the end
ws.append([''])
ws.append(['RMSE AutoARIMA:', rmse(y_AutoArima)])
ws.append(['RMSE AutoRegressive:', rmse(y_AutoRegressive)])
ws.append(['RMSE AutoTheta:', rmse(y_AutoTheta)])
wb.save(excel_file)