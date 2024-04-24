import winsound
import numpy as np

def rmse(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    return np.sqrt(np.mean((y_true - y_pred) ** 2))

y_true = [19.4, 18.7, 15.1,13.7, 14.4]  # actual values
y_AutoArima = [17.315361, 16.874325, 16.178387, 15.372069, 14.842568]  # predicted values
y_AutoETS = [17.299931, 17.299931, 17.299931, 17.299931, 17.299931] # predicted values
y_AutoTheta = [16.435801, 16.202057, 15.875861, 15.367035, 14.857078]
y_CES = [15.459394, 14.832389, 14.873434, 13.318382, 12.311768]

print("RMSE AutoARIMA:", rmse(y_true, y_AutoArima))

print("RMSE AutoETS:", rmse(y_true, y_AutoETS))

print("RMSE AutoTheta:", rmse(y_true, y_AutoTheta))

print("RMSE AutoCES:", rmse(y_true, y_CES))

winsound.Beep(2500, 500)