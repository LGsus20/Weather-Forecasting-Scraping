import LoadMyModel
import numpy as np
import pandas as pd
import LoadMyModel

# Call LoadMyModel.py for predictions
Y_hat_df = LoadMyModel.LoadMyModel()

# ENTER THE ACTUAL VALUES:
y_true = [3.2, 3.6, 4, 2.5, 2.9, 4.3]
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
y_AutoETS = Y_hat_df['AutoETS']
y_AutoTheta = Y_hat_df['AutoTheta']
y_CES = Y_hat_df['CES']

print()
print("RMSE AutoARIMA:", rmse(y_AutoArima))
print("RMSE AutoETS:", rmse(y_AutoETS))
print("RMSE AutoTheta:", rmse(y_AutoTheta))
print("RMSE AutoCES:", rmse(y_CES))
