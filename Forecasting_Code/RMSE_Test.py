import LoadMyModel
import numpy as np

def rmse(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    return np.sqrt(np.mean((y_true - y_pred) ** 2))

Y_hat_df = LoadMyModel.LoadMyModel()

y_true = [3.2, 3.6, 4, 2.5, 2.9, 4.3]  # actual values
y_AutoArima = Y_hat_df['AutoARIMA']  # predicted values
y_AutoETS = Y_hat_df['AutoETS'] # predicted values
y_AutoTheta = Y_hat_df['AutoTheta']
y_CES = Y_hat_df['CES']

print("RMSE AutoARIMA:", rmse(y_true, y_AutoArima))

print("RMSE AutoETS:", rmse(y_true, y_AutoETS))

print("RMSE AutoTheta:", rmse(y_true, y_AutoTheta))

print("RMSE AutoCES:", rmse(y_true, y_CES))
